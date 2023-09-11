#!/usr/bin/python3
"""Defines a class MyInt wich will inherits from int."""


class MyInt(int):
    """Invert the int operators == and !=."""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
