#!/usr/bin/python3
"""Defines aclass-checking function that is inhiritted."""


def inherits_from(obj, a_class):
    """Checks if an inherited instance of a class is the object.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
