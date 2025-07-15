#!/usr/bin/env python3
"""
Test individual scrapers.
Usage: python test_scraper.py [scraper_name] [company_name]

Examples:
  python test_scraper.py crunchbase OpenAI
  python test_scraper.py angellist Anthropic
  python test_scraper.py kaspr Stability AI
  python test_scraper.py googlemaps "Google"
"""

import sys
import logging
import redis
from pathlib import Path

# Add the app directory to Python path
sys.path.insert(0, str(Path(__file__).parent / "app"))

def main():
    if len(sys.argv) < 3:
        print("Usage: python test_scraper.py [scraper_name] [company_name]")
        print("Available scrapers: crunchbase, angellist, kaspr, googlemaps")
        print("Example: python test_scraper.py crunchbase OpenAI")
        return
    
    scraper_name = sys.argv[1].lower()
    company_name = sys.argv[2]
    
    # Setup logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    try:
        # Connect to Redis
        r = redis.Redis(host="localhost", port=6379, db=0)
        r.ping()
        logger.info("✅ Connected to Redis")
    except redis.ConnectionError:
        logger.error("❌ Redis connection failed. Start Redis first.")
        return
    
    # Import and test the specified scraper
    try:
        if scraper_name == "crunchbase":
            from services.scraping.crunchbase import CrunchbaseScraper
            scraper = CrunchbaseScraper(r)
        elif scraper_name == "angellist":
            from services.scraping.angellist import AngelListScraper
            scraper = AngelListScraper(r)
        elif scraper_name == "kaspr":
            from services.scraping.kaspr import KasprScraper
            scraper = KasprScraper(r)
        elif scraper_name == "googlemaps":
            from services.scraping.googlemaps import GoogleMapsScraper
            scraper = GoogleMapsScraper(r)
        else:
            logger.error(f"❌ Unknown scraper: {scraper_name}")
            return
        
        logger.info(f"🔍 Testing {scraper_name} scraper for: {company_name}")
        data = scraper.fetch_company(company_name)
        
        if data:
            logger.info("✅ Success!")
            print(f"\n📊 Results for {company_name}:")
            for key, value in data.items():
                print(f"  {key}: {value}")
        else:
            logger.warning("⚠️  No data returned")
            
    except ImportError as e:
        logger.error(f"❌ Import error: {e}")
    except Exception as e:
        logger.error(f"❌ Error: {e}")

if __name__ == "__main__":
    main() 