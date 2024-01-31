#!/usr/bin/python3
""" LFU Caching """
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """ Create a class LFUCache that inherits from BaseCaching """

    def __init__(self):
        super().__init__()
        self._lfu_keys = []

    def put(self, key, item):
        """ Must assign to the dictionary self.cache_data """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self._lfu_keys.pop(self._lfu_keys.index(key))
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    lfu = self._lfu_keys.pop(0)
                    del self.cache_data[lfu]
                    print(f"DISCARD: {lfu}")
                self.cache_data[key] = item
            self._lfu_keys.append(key)

    def get(self, key):
        """ Must return the value in self.cache_data """
        if key is not None and key in self.cache_data:
            self._lfu_keys.pop(self._lfu_keys.index(key))
            self._lfu_keys.append(key)
        return self.cache_data.get(key, None)
