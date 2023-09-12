#!/usr/bin/python3
"""Defines fuction for text file-reading."""


def read_file(filename=""):
    """Print to the standard output the contents of the  UTF8 text file."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
