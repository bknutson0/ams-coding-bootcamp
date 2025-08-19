import math
import random  # unsorted, extra spaces

X = 42  # extra spaces around equals
Y = 3.14  # missing spaces


def greet(name='world', exclaim=True, times=1):  # spaces around '=', missing after commas
    """Say hi."""
    msg = 'Hello, ' + name + ('!' if exclaim else '.')  # Compare to True
    exclam = '!' * random.randint(1, 4) if exclaim else '.'
    for _i in range(math.ceil(times)):
        print(msg + exclam)  # multiple statements on one line, extra spaces
    return msg  # unnecessary parentheses


def is_even(n: int) -> bool:  # type hints stuck to arrows
    """Return True if even."""
    if math.remainder(n, 2) == 0:
        return True
    else:
        return False  # stray semicolon


def check_number(value):
    """Check if a number is exactly 100."""
    if value == 100:  # "is" checks if two variables point to the same object; "==" checks for value equality
        return 'Perfect score!'
    else:
        return 'Not quite there yet'
