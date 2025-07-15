#!/usr/bin/env python3
"""
Main script to run lead intelligence scrapers.
Run this from the backend directory: python run_scrapers.py
"""

import sys
import os
import logging
import redis
from pathlib import Path
import pprint

# Add the app directory to Python path
sys.path.insert(0, str(Path(__file__).parent / "app"))

from services.scraping.crunchbase import CrunchbaseScraper
from services.scraping.angellist import AngelListScraper
from services.scraping.kaspr import KasprScraper
from services.scraping.googlemaps import GoogleMapsScraper

def main():
    """Run all scrapers with example data."""
    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger(__name__)
    
    try:
        # Connect to Redis
        r = redis.Redis(host="localhost", port=6379, db=0)
        r.ping()  # Test connection
        logger.info("✅ Connected to Redis successfully")
    except redis.ConnectionError:
        logger.error("❌ Failed to connect to Redis. Make sure Redis is running.")
        logger.info("💡 Start Redis with: docker run -d -p 6379:6379 redis:alpine")
        return
    
    # Test companies
    test_companies = ["OpenAI", "Anthropic", "Stability AI"]
    
    # Test each scraper
    scrapers = [
        ("Crunchbase", CrunchbaseScraper(r)),
        ("AngelList", AngelListScraper(r)),
        ("Kaspr", KasprScraper(r)),
        ("Google Maps", GoogleMapsScraper(r))
    ]
    
    for scraper_name, scraper in scrapers:
        logger.info(f"\n🔍 Testing {scraper_name} Scraper:")
        logger.info("=" * 50)
        
        for company in test_companies:
            logger.info(f"\n📊 Fetching data for: {company}")
            try:
                data = scraper.fetch_company(company)
                if data:
                    logger.info(f"✅ Success: {data.get('company_name', company)}")
                    logger.info(f"   Location: {data.get('location', 'N/A')}")
                    logger.info(f"   Website: {data.get('website', 'N/A')}")
                    pprint.pprint(data)
                    if 'description' not in data or not data['description']:
                        logger.warning(f"No description found for {data.get('company_name', company)}. Summarization will be skipped.")
                else:
                    logger.warning(f"⚠️  No data returned for {company}")
            except Exception as e:
                logger.error(f"❌ Error fetching {company}: {e}")
        
        # Test cache hit
        logger.info(f"\n🔄 Testing cache for {scraper_name}:")
        try:
            data = scraper.fetch_company("OpenAI")  # Should hit cache
            if data:
                logger.info("✅ Cache hit successful")
        except Exception as e:
            logger.error(f"❌ Cache test failed: {e}")

if __name__ == "__main__":
    main() 