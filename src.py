from typing import NamedTuple, Any

# sentinel value for marking a deleted object, useful for linear probing
DELETED = object()

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

    def __len__(self):
        return len(self.items)

    def _index(self, key):
        return hash(key) % self.size

    def _probe(self, key):
        # you start by using hashed idx, then, loop through all the available slots
        index = self._index(key)
        for _ in range(self.size):
            yield index, self._items[index]
            index = (index + 1) % self.size

    def __setitem__(self, key, value):
        # linear probing hash collision resolution
        # look next idx until we reach full size
        for idx, pair in self._probe(key):
            if pair is DELETED: continue
            # search
            if pair is None or pair.key == key:
                # update
                self._items[idx] = Pair(key, value)
                break
        else:
            raise MemoryError("not enough size")

    def __getitem__(self, key):
        for _, pair in self._probe(key):
            if pair is None:
                raise KeyError(key)
            if pair is DELETED:
                continue
            if pair.key == key:
                return pair.value
        raise KeyError(key)

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
        for idx, pair in self._probe(key):
            if pair is None:
                raise KeyError(key)
            if pair is DELETED:
                continue
            if pair.key == key:
                self._items[idx] = DELETED
                break
            else:
                raise KeyError(key)

    def __iter__(self):
        yield from self.keys

    def __str__(self):
        pairs = []
        for key, value in self.items:
            pairs.append(f"{key!r}: {value!r}")
        return "{" + ", ".join(pairs) + "}"

    @classmethod
    def from_dict(cls, dictionary, size=None):
        hash_table = cls(size or len(dictionary)*10)
        for key, value in dictionary.items():
            hash_table[key] = value
        return hash_table

    def __repr__(self):
        cls = self.__class__.__name__
        return f"{cls}.from_dict({str(self)})"

    def __eq__(self, other):
        ''' two objects are equal if they have the same set of key-value pairs'''
        if self is other:
            return True
        if type(self) is not type(other):
            return False
        return set(self.items) == set(other.items)

    def copy(self):
        ''' create a new dictionary using the same items and size'''
        return self.from_dict(dict(self.items), size=self.size)

    def update(self, other):
        ''' update a dictionary with items from other, in case both have same key, keep other value '''
        if not isinstance(other, HashTable):
            raise TypeError
        if not other:
            return self
        for key, value in other.items:
            self[key] = value

    def __or__(self, other):
        if not isinstance(other, HashTable):
            raise TypeError
        new = self.copy()
        new.update(other)
        return new

    def __ror__(self, other):
        ''' right union, in case left object doesn't have __or__ method '''
        if not isinstance(other, HashTable):
            raise TypeError
        new = self.copy()
        new.update(other)
        return new

    def __ior__(self, other):
        ''' in-place union '''
        self.update(other)
        return self


