import math
import random

X = 42
Y = 3.14


def greet(name='world', exclaim=True, times=1):
    """Say hi."""
    msg = 'Hello, ' + name + ('!' if exclaim else '.')
    exclam = '!' * random.randint(1, 4) if exclaim else '.'
    for _i in range(math.ceil(times)):
        print(msg + exclam)
    return msg


def is_even(n: int) -> bool:
    """Return True if even."""
    return math.remainder(n, 2) == 0


def check_number(value):
    """Check if a number is exactly 100."""
    if value == 100:
        return 'Perfect score!'
    else:
        return 'Not quite there yet'
