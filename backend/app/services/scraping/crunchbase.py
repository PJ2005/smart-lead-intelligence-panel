from .base import BaseScraper
import json
from typing import Any, Dict, Optional
import redis
import logging
import requests

class CrunchbaseScraper(BaseScraper):
    """
    Scraper for Crunchbase company and founder data with Redis caching.
    """
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
            self.redis.setex(cache_key, self.cache_ttl, json.dumps(normalized))
            self._store_in_db(normalized)
            return normalized
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