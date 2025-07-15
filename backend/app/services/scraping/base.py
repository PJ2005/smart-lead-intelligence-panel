import logging
from typing import Any, Dict, Optional
import redis
from abc import ABC, abstractmethod

class BaseScraper(ABC):
    """
    Abstract base class for all lead scrapers.
    Enforces OOP, Redis caching, and logging patterns.
    """
    def __init__(self, redis_client: redis.Redis, cache_ttl: int = 3600):
        self.redis = redis_client
        self.cache_ttl = cache_ttl
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    def fetch_company(self, company_name: str) -> Optional[Dict[str, Any]]:
        """
        Fetch and normalize company data, using Redis cache.
        """
        pass

    @abstractmethod
    def _scrape_company(self, company_name: str) -> Optional[Dict[str, Any]]:
        """
        Scrape or fetch company data from the source.
        """
        pass

    @abstractmethod
    def parse_company(self, raw: Dict[str, Any]) -> Dict[str, Any]:
        """
        Parse raw data into a structured dict.
        """
        pass

    @abstractmethod
    def normalize_company(self, parsed: Dict[str, Any]) -> Dict[str, Any]:
        """
        Normalize parsed data to the internal company schema.
        """
        pass

    def _store_in_db(self, company: Dict[str, Any]) -> None:
        """
        Store the normalized company data in the database (stub).
        """
        # TODO: Implement actual DB storage
        self.logger.info(f"Stub: storing company in DB: {company.get('company_name')}") 