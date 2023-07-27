#!/usr/bin/env python3
""" a class FIFOCache that inherits
from BaseCaching and is a caching system
"""


from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """ a class FIFOCache that inherits
    from BaseCaching and is a caching system
    """
    def __init__(self):
        """Inherit from parent"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """"put() function"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_item, _last_item = self.cache_data.popitem()
            # Or first_item_deleted = self.cache_data.pop(0)
            print("DISCARD: {}".format(first_item))

    def get(self, key):
        """get() function"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
        # or self.cache_data.get(key, None)
