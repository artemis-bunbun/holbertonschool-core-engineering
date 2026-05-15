#!/usr/bin/env python3
"""Rectangle class built on BaseGeometry."""

BaseGeometry = __import__("base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle defined by width and height."""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the rectangle area."""
        return self.__width * self.__height

    def __str__(self):
        """Return a readable rectangle description."""
        return f"[Rectangle] {self.__width}/{self.__height}"
