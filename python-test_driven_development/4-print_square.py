#!/usr/bin/python3
"""This module provides a function that prints a square using # characters.

The function validates the size input and raises appropriate exceptions
for invalid types or values.
"""


def print_square(size):
    """Prints a square of # characters with the given size.

    Raises TypeError if size is not an integer, ValueError if size < 0.
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
