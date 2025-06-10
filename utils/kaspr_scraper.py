import os
import requests
from bs4 import BeautifulSoup
import redis
import backoff
import hashlib
import json
from datetime import timedelta

KASPR_API_KEY = os.getenv("KASPR_API_KEY")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
REDIS_TTL = 60 * 60 * 24  # 24 hours

redis_client = redis.Redis.from_url(REDIS_URL)

def cache_key(url):
    return f"kaspr:linkedin:{hashlib.sha256(url.encode()).hexdigest()}"

def extract_exit_intent(job_history):
    # Example heuristic: founder has left or changed roles recently
    for job in job_history:
        if "founder" in job.get("title", "").lower() and job.get("end_date"):
            return True
    return False

def parse_job_history(kaspr_data):
    jobs = []
    for exp in kaspr_data.get("experiences", []):
        jobs.append({
            "title": exp.get("title"),
            "company": exp.get("company"),
            "start_date": exp.get("start_date"),
            "end_date": exp.get("end_date"),
        })
    return jobs

@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=5)
def fetch_kaspr_profile(linkedin_url):
    headers = {"x-api-key": KASPR_API_KEY}
    resp = requests.get(
        "https://api.kaspr.io/v1/linkedin/profile",
        params={"url": linkedin_url},
        headers=headers,
        timeout=15
    )
    resp.raise_for_status()
    return resp.json()

def scrape_linkedin_profile(url: str) -> dict:
    """
    Example input: "https://linkedin.com/in/johndoe"
    Expected output: {
        name: "John Doe",
        current_role: "CEO at Acme Corp",
        job_history: [...],
        exit_intent: True,
        gdpr_badge: "✅ Compliant"
    }
    """
    key = cache_key(url)
    cached = redis_client.get(key)
    if cached:
        return json.loads(cached)

    kaspr_data = fetch_kaspr_profile(url)
    name = kaspr_data.get("full_name")
    current_role = kaspr_data.get("current_position")
    job_history = parse_job_history(kaspr_data)
    exit_intent = extract_exit_intent(job_history)
    gdpr_badge = "✅ Compliant"  # Kaspr is GDPR compliant

    result = {
        "name": name,
        "current_role": current_role,
        "job_history": job_history,
        "exit_intent": exit_intent,
        "gdpr_badge": gdpr_badge
    }
    redis_client.setex(key, timedelta(seconds=REDIS_TTL), json.dumps(result))
    return result
