### 2024-12-19 - Added KasprScraper, AngelListScraper, GoogleMapsScraper

- Added `KasprScraper` (LinkedIn via Kaspr API), `AngelListScraper`, and `GoogleMapsScraper` to `app/services/scraping/`.
- All scrapers inherit from `BaseScraper` for OOP, Redis caching, and logging consistency.
- Each scraper implements `fetch_company`, `_scrape_company`, `parse_company`, and `normalize_company`.
- All modules are independently testable and follow the same usage pattern.
- No major issues; stubbed API responses for now. Real API integration is a future step.
- Updated backend README with usage and structure for all scrapers.
- No changes required to other modules; scraping system remains modular and extensible. 