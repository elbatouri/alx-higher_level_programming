#!/usr/bin/python3
"""Defines a function that is a file-appending function."""


def append_write(filename="", text=""):
    """Add to the end of a UTF8 text file a string.

    Args:
        filename (str): The file's name to append to.
        text (str): The string to add to the file.
    Returns:
        The number of the appended characters.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
