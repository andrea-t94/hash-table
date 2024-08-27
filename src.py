from typing import NamedTuple, Any

class Pair(NamedTuple):
    # tuple that guarantees immutability for any data type
    key: Any
    value: Any

class HashTable:
    def __init__(self, size):
        # fixed size established at creation time
        if not isinstance(size, int):
            raise TypeError(f"Invalid input type: {type(size).__name__}. Expected int.")
        if size < 1:
            raise ValueError("Capacity must be a positive number")
        self._size = size
        # initialize empty value slots
        # None can be used since we expect tuples as non-empty values
        self._items = [None] * self._size

    def __len__(self):
        return len(self.items)

    def _index(self, key):
        return hash(key) % len(self._items)

    def __setitem__(self, key, value):
        idx = self._index(key)
        # hash collision not taken into account
        self._items[idx] = Pair(key, value)

    def __getitem__(self, key):
        idx = self._index(key)
        pair = self._items[idx]
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
            self._items[self._index(key)] = None
        else:
            raise KeyError(key)

    @property
    def items(self):
        # defensive copying
        return {pair for pair in self._items if pair}

    @property
    def values(self):
        # list gives me duplicates
        return [pair.value for pair in self.items]

    @property
    def keys(self):
        return {pair.key for pair in self.items}

    @property
    def size(self):
        return self._size
