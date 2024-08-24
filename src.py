from typing import NamedTuple, Any

class Pair(NamedTuple):
    # tuple that guarantees immutability for any data type
    key: Any
    value: Any

class HashTable:
    def __init__(self, size):
        # fixed size established at creation time
        self.size = size
        # initialize empty value slots
        # None can be used since we expect tuples as non-empty values
        self.items = [None] * self.size

    def __len__(self):
        return len(self.items)

    def _index(self, key):
        return hash(key) % len(self)

    def __setitem__(self, key, value):
        idx = self._index(key)
        # hash collision not taken into account
        self.items[idx] = Pair(key, value)

    def __getitem__(self, key):
        idx = self._index(key)
        pair = self.items[idx]
        if pair is None:
            raise KeyError(key)
        return pair.value

    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __delitem__(self, key):
        if key in self:
            # cannot use __setitem__ since None would be wrapped into a tuple
            # thus the item won't be considered deleted
            self.items[self._index(key)] = None
        else:
            raise KeyError(key)
