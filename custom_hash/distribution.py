from collections import Counter
from typing import List, Callable

def distribute(items: List, bins: int, hash_function: Callable = hash) -> Counter:
    ''' it returns the distribution of the hashed items
        - items: list of items to be hashed
        - bins: number of bins
        - hash_function: it can be any hash function
    '''
    return Counter([hash_function(item) % bins for item in items])

def plot(histogram: Counter) -> None:
    ''' plot the distribution as histogram '''
    for key in sorted(histogram):
        count = histogram[key]
        padding = (max(histogram.values()) - count) * " "
        print(f"{key:3} {'■' * count}{padding} ({count})")