from distribution import plot, distribute
from src import custom_hash
from string import printable

print(plot(distribute(printable, 6, custom_hash)))
