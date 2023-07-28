#!/usr/bin/env python3
""" a class MRUCache that inherits
from BaseCaching and is a caching system
"""


from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ a class LIFOCache that inherits
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
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru, _ = self.cache_data.popitem(False)
                # Or first_item_deleted = self.cache_data.pop(0)
                print("DISCARD: {}".format(mru))
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """get() function"""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        # return self.cache_data[key]
        return self.cache_data.get(key, None)
