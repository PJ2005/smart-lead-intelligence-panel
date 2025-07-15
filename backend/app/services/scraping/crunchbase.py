import os
from dotenv import load_dotenv
load_dotenv()
from .base import BaseScraper
import json
from typing import Any, Dict, Optional
import redis
import logging
import requests
from app.services.enrichment.enrichment import EnrichmentService

class CrunchbaseScraper(BaseScraper):
    """
    Scraper for Crunchbase company and founder data with Redis caching and enrichment.
    """
    def __init__(self, redis_client: redis.Redis, cache_ttl: int = 3600):
        super().__init__(redis_client, cache_ttl)
        self.enrichment_service = EnrichmentService(
            apollo_enrichment_api_key=os.environ.get('APOLLO_ENRICHMENT_API_KEY')
        )

    def fetch_company(self, company_name: str) -> Optional[Dict[str, Any]]:
        cache_key = f"crunchbase:company:{company_name.lower()}"
        try:
            cached = self.redis.get(cache_key)
            if cached:
                self.logger.info(f"Cache hit for {company_name}")
                return json.loads(cached)
            self.logger.info(f"Cache miss for {company_name}, scraping...")
            raw = self._scrape_company(company_name)
            if not raw:
                self.logger.warning(f"No data found for {company_name}")
                return None
            parsed = self.parse_company(raw)
            normalized = self.normalize_company(parsed)
            # Enrich the normalized data
            enriched = self.enrichment_service.enrich(normalized)
            self.redis.setex(cache_key, self.cache_ttl, json.dumps(enriched))
            self._store_in_db(enriched)
            return enriched
        except Exception as e:
            self.logger.error(f"Error fetching company {company_name}: {e}")
            return None

    def _scrape_company(self, company_name: str) -> Optional[Dict[str, Any]]:
        try:
            # Stubbed response for demonstration:
            return {
                "name": company_name,
                "description": f"{company_name} is a leading company in AI.",
                "founders": [
                    {"name": "Sam Altman", "role": "CEO"},
                    {"name": "Greg Brockman", "role": "President"}
                ],
                "website": f"https://{company_name.lower()}.com",
                "location": "San Francisco, CA",
                "founded": 2015
            }
        except Exception as e:
            self.logger.error(f"Scraping error for {company_name}: {e}")
            return None

    def parse_company(self, raw: Dict[str, Any]) -> Dict[str, Any]:
        return raw

    def normalize_company(self, parsed: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "company_name": parsed.get("name"),
            "description": parsed.get("description"),
            "founders": [f["name"] for f in parsed.get("founders", [])],
            "website": parsed.get("website"),
            "location": parsed.get("location"),
            "founded_year": parsed.get("founded"),
        }

# Usage Example
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    r = redis.Redis(host="localhost", port=6379, db=0)
    scraper = CrunchbaseScraper(r)
    data = scraper.fetch_company("OpenAI")
    print(data) 