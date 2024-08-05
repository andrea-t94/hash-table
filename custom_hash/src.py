from typing import Protocol

class Stringifiable(Protocol):
    def __str__(self) -> str:
        ...

def custom_hash(key: Stringifiable, maxSize: int = 1000) -> int:
    ''' it  returns the hash function
        - key: any python object that implements a textual representation
        - maxSize: maximum lenght of the hash function
        '''
    return sum(
        index * ord(character)
        for index, character in enumerate(repr(key), start=1)
    ) % maxSize