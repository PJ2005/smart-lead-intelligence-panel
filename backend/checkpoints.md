## 2024-12-19 - Milestone: CrunchbaseScraper Implemented

- Implemented the first multi-source scraping module: CrunchbaseScraper (OOP, Python)
- Integrated Redis caching to avoid redundant requests
- Added robust error handling and logging
- Stubbed DB storage for future SQLAlchemy integration
- Updated backend README with usage and structure
- Updated developer.md and design.md with rationale and details
- Structure is ready for additional sources (just add new class in scraping/)

Commit message:
"feat(backend/scraping): add CrunchbaseScraper with OOP, Redis caching, error handling, and extensibility" 

## 2024-12-19 - Milestone: KasprScraper Implemented
- Added KasprScraper (LinkedIn via Kaspr API) with OOP, Redis caching, and logging.
- Follows BaseScraper interface and is independently testable.
- Stubbed API response for now.
Commit message:
"feat(backend/scraping): add KasprScraper (LinkedIn) with OOP, Redis caching, and logging"

## 2024-12-19 - Milestone: AngelListScraper Implemented
- Added AngelListScraper with OOP, Redis caching, and logging.
- Follows BaseScraper interface and is independently testable.
- Stubbed API response for now.
Commit message:
"feat(backend/scraping): add AngelListScraper with OOP, Redis caching, and logging"

## 2024-12-19 - Milestone: GoogleMapsScraper Implemented
- Added GoogleMapsScraper with OOP, Redis caching, and logging.
- Follows BaseScraper interface and is independently testable.
- Stubbed API response for now.
Commit message:
"feat(backend/scraping): add GoogleMapsScraper with OOP, Redis caching, and logging" 