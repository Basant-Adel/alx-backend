#!/usr/bin/python3
""" FIFO caching """
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """ Create a class FIFOCache that inherits from BaseCaching """

    def put(self, key, item):
        """ Must assign to the dictionary self.cache_data """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                discarded_key = sorted(self.cache_data.keys())[0]
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """ Must return the value in self.cache_data """
        return self.cache_data.get(key, None)
