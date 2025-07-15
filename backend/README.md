# Backend Module (Python/FastAPI)

The backend provides the server-side logic, APIs, and business intelligence for the Lead Intelligence Panel. It is implemented in Python using FastAPI, with a modular, OOP-friendly structure.

## 🏗️ Architecture

### Core Components
- **API Layer** (`app/api/`): RESTful endpoints (FastAPI routers)
- **Services** (`app/services/`): Business logic and domain services (OOP, feature-based)
- **Models** (`app/models/`): SQLAlchemy ORM models
- **Schemas** (`app/schemas/`): Pydantic models for validation
- **Repositories** (`app/repositories/`): Data access layer
- **Core** (`app/core/`): App config, settings, startup logic
- **Utils** (`app/utils/`): Utility functions
- **Caching**: Redis integration for API, session, and scraping result caching

### Scraping Modules
Each scraping source (e.g., Crunchbase) is implemented as a class in its own module under `app/services/scraping/`.

#### Example: Crunchbase Scraper
- `app/services/scraping/crunchbase.py`
- Class: `CrunchbaseScraper`
- Methods: `fetch_company`, `parse_company`, `normalize_company`, `fetch_founder`, etc.
- Uses Redis to cache results and avoid redundant requests
- Results are stored in the database (or stubbed for now)

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- PostgreSQL 14+
- Redis 7+
- pip

### Installation

1. **Install dependencies**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

2. **Set up environment variables**
   ```bash
   cp ../env.example .env
   # Edit .env with your configuration
   ```

3. **Run the server**
   ```bash
   uvicorn app.main:app --reload
   ```

4. **API Docs**
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## 🧩 Scraping Module Usage

### CrunchbaseScraper
Implements OOP scraping for Crunchbase with Redis caching and robust error handling.

**Usage Example:**
```python
from app.services.scraping.crunchbase import CrunchbaseScraper
import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0)
scraper = CrunchbaseScraper(redis_client)
company_data = scraper.fetch_company("OpenAI")
print(company_data)
```

### KasprScraper (LinkedIn via Kaspr API)
OOP scraper for LinkedIn company data via Kaspr API, with Redis caching and logging.

**Usage Example:**
```python
from app.services.scraping.kaspr import KasprScraper
import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0)
scraper = KasprScraper(redis_client)
company_data = scraper.fetch_company("ExampleCorp")
print(company_data)
```

### AngelListScraper
OOP scraper for AngelList company/founder data, with Redis caching and logging.

**Usage Example:**
```python
from app.services.scraping.angellist import AngelListScraper
import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0)
scraper = AngelListScraper(redis_client)
company_data = scraper.fetch_company("FintechStartup")
print(company_data)
```

### GoogleMapsScraper
OOP scraper for company location/details via Google Maps API, with Redis caching and logging.

**Usage Example:**
```python
from app.services.scraping.googlemaps import GoogleMapsScraper
import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0)
scraper = GoogleMapsScraper(redis_client)
company_data = scraper.fetch_company("Google")
print(company_data)
```

**All scrapers inherit from `BaseScraper` and follow the same OOP, caching, and logging patterns.**

**To add a new source:** Create a new class in `app/services/scraping/` inheriting from `BaseScraper`.

## 📁 Directory Structure

```
backend/
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   │   └── scraping/
│   │       └── crunchbase.py
│   ├── repositories/
│   └── utils/
├── tests/
├── requirements.txt
└── README.md
```

## 🛠️ Development

- **Linting**: `flake8` and `black`
- **Testing**: `pytest`
- **Type Checking**: `mypy`
- **Pre-commit**: `pre-commit`

## 🔄 Extending Scraping
To add a new source, create a new class in `app/services/scraping/` and follow the OOP pattern. Register the new scraper in the scraping service registry.

---

**Last updated:** 2024-12-19 