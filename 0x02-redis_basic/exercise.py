#!/usr/bin/env python3
"""Define the Cache class"""
import redis
from typing import Union, Callable
import uuid


class Cache():
    """This class is an abstraction layers to a redis client"""
    def __init__(self):
        """Initialize the redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[int, float, str]) -> str:
        """store the input data in Redis using a random key and
        return the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn=None: Callable) -> None:
        """convert the data back to the desired forma"""

    def get_str(self, data: byte) -> str:
        """Return a string version of data"""

    def get_int(self, data)
