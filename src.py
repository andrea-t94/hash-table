class Blank:
    pass

class HashTable:
    def __init__(self, size):
        # fixed size established at creation time
        self.size = size
        # initialize empty value slots
        self.values = [Blank] * self.size

    def __len__(self):
        return len(self.values)

    def _index(self, key):
        return hash(key) % len(self)

    def __setitem__(self, key, value):
        idx = self._index(key)
        # hash collision not taken into account
        self.values[idx] = value

    def __getitem__(self, key):
        idx = self._index(key)
        value = self.values[idx]
        if value is Blank:
            raise KeyError(key)
        return value

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
            self[key] = Blank
        else:
            raise KeyError(key)
