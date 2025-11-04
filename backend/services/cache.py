"""
Simple in-memory cache stub for reports.

This cache implementation is not persisted across restarts and should
only be used for demonstration.  Real caches might use Redis or
PostgreSQL tables with TTL semantics.
"""

from typing import Any, Dict, Optional
import time


class InMemoryCache:
    """A naive in-memory TTL cache."""

    def __init__(self, default_ttl: int = 30 * 24 * 60 * 60) -> None:
        self.default_ttl = default_ttl
        self._store: Dict[str, tuple[float, Any]] = {}

    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        """Store a value with an optional TTL override."""
        expiry = time.time() + (ttl or self.default_ttl)
        self._store[key] = (expiry, value)

    def get(self, key: str) -> Optional[Any]:
        """Retrieve a value if it has not expired."""
        item = self._store.get(key)
        if item is None:
            return None
        expiry, value = item
        if expiry < time.time():
            del self._store[key]
            return None
        return value