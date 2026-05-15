#!/usr/bin/env python3
"""Square class built on Rectangle."""

Rectangle = __import__("2-rectangle").Rectangle


class Square(Rectangle):
    """Represent a square as a specialized rectangle."""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
