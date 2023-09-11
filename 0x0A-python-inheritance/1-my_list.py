#!/usr/bin/python3
"""Defines class MyList an inheretted list."""


class MyList(list):
    """Implements sorted printing."""

    def print_sorted(self):
        """Print a list wich sorted by ascending order."""
        print(sorted(self))
