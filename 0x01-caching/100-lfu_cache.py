#!/usr/bin/env python3
"""LFUChacing"""

from collections import defaultdict, OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class is a caching system that
    implements the Least Frequently Used (LFU) caching algorithm.

    Attributes:
        cache_data (dict): A dictionary to
        store key-value pairs as the cache.
        freq_map (defaultdict): A dictionary of OrderedDicts
        to store keys based on their usage frequency.
        key_freq (defaultdict): A dictionary to
        store the frequency of each key in the cache.

    Methods:
        __init__(): Constructor method. Initializes
        the LFUCache object and the parent BaseCaching.
        update_frequency(key): Helper method to
        update the usage frequency of a key.

        evict(): Helper method to evict the least
        frequently used item from the cache.
        put(key, item): Adds a key-value pair
        to the cache using the LFU algorithm.
        get(key): Retrieves the value of a
        key from the cache using the LFU algorithm.
    """

    def __init__(self):
        """
        Constructor method for LFUCache class.

        Initializes the LFUCache object and calls
        the constructor of the parent BaseCaching class.
        It also initializes the freq_map and
        key_freq dictionaries for tracking frequency of items.
        """
        super().__init__()
        self.freq_map = defaultdict(OrderedDict)
        self.key_freq = defaultdict(int)

    def update_frequency(self, key):
        """
        Helper method to update the usage frequency of a key.

        Args:
            key: The key whose frequency needs to be updated.

        This method increases the usage
        frequency of the given key by 1.
        It moves the key from its current
        frequency to the new frequency in the freq_map dictionary.
        """
        current_freq = self.key_freq[key]
        new_freq = current_freq + 1

        # Move the key from the current frequency to the new frequency
        self.freq_map[current_freq].pop(key)
        self.freq_map[new_freq][key] = self.cache_data[key]

        # Update the frequency of the key in the key_freq dictionary
        self.key_freq[key] = new_freq

        # If the previous frequency has no keys, remove it from the freq_map
        if not self.freq_map[current_freq]:
            del self.freq_map[current_freq]

    def evict(self):
        """
        Helper method to evict the least
        frequently used item from the cache.

        This method finds the least frequently
        used key and its frequency in the freq_map dictionary.
        It then removes the LFU key from the cache,
        the key_freq dictionary, and the freq_map dictionary.
        """
        # Find the least frequently used key and its frequency
        min_freq = min(self.freq_map.keys())
        lfu_key = next(iter(self.freq_map[min_freq]))

        # Remove the LFU key from the cache
        del self.cache_data[lfu_key]
        del self.key_freq[lfu_key]

        # Remove the LFU key from the freq_map
        self.freq_map[min_freq].pop(lfu_key)

    def put(self, key, item):
        """
        Adds a key-value pair to the cache using the LFU algorithm.

        Args:
            key: The key to be added to the cache.
            item: The value associated with the key.

        If key or item is None, this method does nothing.
        If the cache is full, it evicts the least
        frequently used item before adding the new key-value pair.
        The method also updates the usage
        frequency of the key after adding it to the cache.
        """
        if key is None or item is None:
            return

        # Check if the key already exists in the cache
        if key in self.cache_data:
            # Update the item value and frequency
            self.cache_data[key] = item
            self.update_frequency(key)
        else:
            # If the cache is full, evict the LFU item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.evict()

            # Add the new key to the cache with frequency 1
            self.cache_data[key] = item
            self.key_freq[key] = 1
            self.freq_map[1][key] = item

    def get(self, key):
        """
        Retrieves the value of a key from the cache using the LFU algorithm.

        Args:
            key: The key whose value needs to be retrieved.

        If key is None or if the key doesn’t exist
        in the cache, it returns None.
        If the key is found, it updates the usage
        frequency of the key and returns the associated value.
        """
        if key is None or key not in self.cache_data:
            return None

        # Update the frequency of the accessed item
        self.update_frequency(key)

        return self.cache_data[key]
