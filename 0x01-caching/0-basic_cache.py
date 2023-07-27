#!/usr/bin/env python3
""" a class BasicCache that inherits from
BaseCaching and is a caching system
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class """
    def put(self, key, item):
        """put() function"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """get() function"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
