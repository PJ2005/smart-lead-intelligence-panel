from .base import BaseScraper
import json
from typing import Any, Dict, Optional
import redis
import logging
import requests

class AngelListScraper(BaseScraper):
    """
    Scraper for AngelList company and founder data with Redis caching.
    """
    def fetch_company(self, company_name: str) -> Optional[Dict[str, Any]]:
        cache_key = f"angellist:company:{company_name.lower()}"
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
            # Stub: Replace with real AngelList API call
            # resp = requests.get("https://api.angel.co/1/startups/search", params={"query": company_name}, headers={...})
            # if resp.status_code == 200:
            #     return resp.json()
            # else:
            #     return None
            return {
                "name": company_name,
                "angellist_url": f"https://angel.co/company/{company_name.lower()}",
                "industry": "Fintech",
                "stage": "Seed",
                "location": "New York, NY",
                "founders": [
                    {"name": "Alex Founder", "role": "CEO"}
                ]
            }
        except Exception as e:
            self.logger.error(f"AngelList scraping error for {company_name}: {e}")
            return None

    def parse_company(self, raw: Dict[str, Any]) -> Dict[str, Any]:
        return raw

    def normalize_company(self, parsed: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "company_name": parsed.get("name"),
            "angellist_url": parsed.get("angellist_url"),
            "industry": parsed.get("industry"),
            "stage": parsed.get("stage"),
            "location": parsed.get("location"),
            "founders": [f["name"] for f in parsed.get("founders", [])],
        }

# Usage Example
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    r = redis.Redis(host="localhost", port=6379, db=0)
    scraper = AngelListScraper(r)
    data = scraper.fetch_company("FintechStartup")
    print(data) 