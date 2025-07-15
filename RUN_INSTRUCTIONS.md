# How to Run the Lead Intelligence Platform

## Prerequisites

- Python 3.10+ installed
- Redis server running (see Redis setup below)
- pip package manager

## 1. Redis Setup

### Option A: Docker (Recommended)
```bash
docker run -d -p 6379:6379 redis:alpine
```

### Option B: Windows Native
Download and install from: https://github.com/microsoftarchive/redis/releases

### Option C: WSL (Windows Subsystem for Linux)
```bash
sudo apt-get install redis-server
sudo service redis-server start
```

## 2. Backend Setup

```bash
cd backend
pip install -r requirements.txt
```

## 3. Running the Scrapers

### Test All Scrapers
```bash
cd backend
python run_scrapers.py
```

### Test Individual Scrapers
```bash
cd backend
python test_scraper.py crunchbase OpenAI
python test_scraper.py angellist Anthropic
python test_scraper.py kaspr "Stability AI"
python test_scraper.py googlemaps "Google"
```

### Available Scrapers
- `crunchbase` - Company and founder data
- `angellist` - Startup and investor data  
- `kaspr` - LinkedIn contact data
- `googlemaps` - Business location data

## 4. Expected Output

You should see:
- ✅ Redis connection success
- 📊 Company data being fetched
- 🔄 Cache hits on subsequent requests
- 📝 Logging of all operations

## 5. Troubleshooting

### Import Error
If you see "ImportError: attempted relative import with no known parent package":
- **Don't run scraper files directly** (e.g., `python crunchbase.py`)
- Use the provided scripts: `python run_scrapers.py` or `python test_scraper.py`

### Redis Connection Error
If Redis connection fails:
- Make sure Redis is running: `docker ps` (if using Docker)
- Check Redis is on port 6379
- Restart Redis if needed: `docker restart <redis-container-id>`

### Missing Dependencies
If you get import errors:
```bash
cd backend
pip install -r requirements.txt
```

## 6. Next Steps

- Add real API keys to `.env` file
- Implement actual database storage
- Set up FastAPI server
- Connect frontend components

---
