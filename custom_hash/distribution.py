from collections import Counter
from typing import List, Callable

def distribute(items: List, num_containers: int, hash_function: Callable = hash) -> Counter:
    return Counter([hash_function(item) % num_containers for item in items])

def plot(histogram: Counter) -> None:
    for key in sorted(histogram):
        count = histogram[key]
        padding = (max(histogram.values()) - count) * " "
        print(f"{key:3} {'■' * count}{padding} ({count})")