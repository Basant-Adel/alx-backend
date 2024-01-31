#!/usr/bin/python3
""" Basic dictionary """
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache """

    def put(self, key, item):
        """ Put """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get """
        return self.cache_data.get(key, None)
