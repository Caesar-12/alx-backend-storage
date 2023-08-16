#!/usr/bin/env python3
"""Contains Cache class"""

import redis
import uuid
from typing import Union


class Cache:
    """A simple cache"""
    def __init__(self) -> None:
        """Constructor function"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[bytes, str, float, int]) -> str:
        """Store methods; takes a data and returns a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
