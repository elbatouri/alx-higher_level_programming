#!/usr/bin/python3
"""Defines the class of the  Rectangle."""


class Rectangle:
    """Represent the rectangle."""

    def __init__(self, width=0, height=0):
        """starts a new Rectangle.

        Args:
            width (int): The width of the initialised rectangle.
            height (int): The height of the initialised rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """enter the rectangle's width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """enter the rectangle's height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
