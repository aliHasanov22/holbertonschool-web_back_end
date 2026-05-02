#!/usr/bin/env python3
"""Redis cache module"""

import redis
import uuid
from typing import Union, Optional, Callable, Any


class Cache:
    """Cache class using Redis"""

    def __init__(self) -> None:
        """Initialize Redis client and flush the database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis using a random key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self,
        key: str,
        fn: Optional[Callable[[bytes], Any]] = None
    ) -> Union[str, bytes, int, float, None]:
        """Retrieve data from Redis and optionally convert it"""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve a string value from Redis"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve an integer value from Redis"""
        return self.get(key, fn=int)