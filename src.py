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

    def __setitem__(self, key, value):
        idx = hash(key) % len(self)
        # hash collision not taken into account
        self.values[idx] = value