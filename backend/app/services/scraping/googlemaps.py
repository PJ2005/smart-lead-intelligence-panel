from .base import BaseScraper
import json
from typing import Any, Dict, Optional
import redis
import logging
import requests

class GoogleMapsScraper(BaseScraper):
    """
    Scraper for company location and details via Google Maps API with Redis caching.
    """
    def fetch_company(self, company_name: str) -> Optional[Dict[str, Any]]:
        cache_key = f"googlemaps:company:{company_name.lower()}"
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
            # Stub: Replace with real Google Maps API call
            # resp = requests.get("https://maps.googleapis.com/maps/api/place/findplacefromtext/json", params={...})
            # if resp.status_code == 200:
            #     return resp.json()
            # else:
            #     return None
            return {
                "name": company_name,
                "address": "1600 Amphitheatre Parkway, Mountain View, CA",
                "website": f"https://{company_name.lower()}.com",
                "phone": "+1 650-253-0000",
                "location": {"lat": 37.422, "lng": -122.084},
                "googlemaps_url": f"https://maps.google.com/?q={company_name}"
            }
        except Exception as e:
            self.logger.error(f"Google Maps scraping error for {company_name}: {e}")
            return None

    def parse_company(self, raw: Dict[str, Any]) -> Dict[str, Any]:
        return raw

    def normalize_company(self, parsed: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "company_name": parsed.get("name"),
            "address": parsed.get("address"),
            "website": parsed.get("website"),
            "phone": parsed.get("phone"),
            "location": parsed.get("location"),
            "googlemaps_url": parsed.get("googlemaps_url"),
        }

# Usage Example
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    r = redis.Redis(host="localhost", port=6379, db=0)
    scraper = GoogleMapsScraper(r)
    data = scraper.fetch_company("Google")
    print(data) 