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

class KasprScraper(BaseScraper):
    """
    Scraper for LinkedIn data via Kaspr API with Redis caching and enrichment.
    """
    def __init__(self, redis_client: redis.Redis, cache_ttl: int = 3600):
        super().__init__(redis_client, cache_ttl)
        self.enrichment_service = EnrichmentService(
            apollo_enrichment_api_key=os.environ.get('APOLLO_ENRICHMENT_API_KEY')
        )

    def fetch_company(self, company_name: str) -> Optional[Dict[str, Any]]:
        cache_key = f"kaspr:company:{company_name.lower()}"
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
            # Stub: Replace with real Kaspr API call
            # resp = requests.get("https://api.kaspr.io/v1/company", params={"name": company_name}, headers={...})
            # if resp.status_code == 200:
            #     return resp.json()
            # else:
            #     return None
            return {
                "name": company_name,
                "linkedin_url": f"https://linkedin.com/company/{company_name.lower()}",
                "industry": "Software",
                "employees": 120,
                "location": "London, UK",
                "contacts": [
                    {"name": "Jane Doe", "role": "CTO", "email": "jane@company.com"}
                ]
            }
        except Exception as e:
            self.logger.error(f"Kaspr scraping error for {company_name}: {e}")
            return None

    def parse_company(self, raw: Dict[str, Any]) -> Dict[str, Any]:
        return raw

    def normalize_company(self, parsed: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "company_name": parsed.get("name"),
            "linkedin_url": parsed.get("linkedin_url"),
            "industry": parsed.get("industry"),
            "employees": parsed.get("employees"),
            "location": parsed.get("location"),
            "contacts": [c["name"] for c in parsed.get("contacts", [])],
        }

# Usage Example
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    r = redis.Redis(host="localhost", port=6379, db=0)
    scraper = KasprScraper(r)
    data = scraper.fetch_company("ExampleCorp")
    print(data) 