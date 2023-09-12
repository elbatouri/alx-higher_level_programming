#!/usr/bin/python3
"""Defines a function that insert text file."""


def append_after(filename="", search_string="", new_string=""):
    """Insert after each line containing a given string in a file a text.

    Args:
        filename (str): The file's name.
        search_string (str): The searched string for within the file.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
