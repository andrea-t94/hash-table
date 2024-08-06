from typing import Protocol

class Stringifiable(Protocol):
    def __str__(self) -> str:
        ...

def custom_hash(key: Stringifiable, maxSize: int = 1000) -> int:
    ''' it returns the hashed key
        - key: any python object that implements a textual representation
        - maxSize: maximum lenght of the hash function
        '''
    return sum(
        index * ord(character)
        # __repr__ add "" to textual repr --> makes the hashed value to be mostly an even number
        # dropping one of them makes the hash function more equally distributed
        for index, character in enumerate(repr(key).lstrip("'"), start=1)
    ) % maxSize