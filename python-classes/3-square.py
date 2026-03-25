#!/usr/bin/python3
"""Module that defines a Square class with area method"""


class Square:
    """Class that defines a square by its size with area computation"""

    def __init__(self, size=0):
        """Initialize a new Square instance

        Args:
            size (int): size of the square, defaults to 0

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square

        Returns:
            int: area of the square
        """
        return self.__size ** 2
