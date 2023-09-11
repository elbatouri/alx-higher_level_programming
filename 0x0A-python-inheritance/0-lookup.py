#!/usr/bin/python3
"""Defines lookup function."""


def lookup(obj):
    """Return a list of available attributesof the object."""
    return (dir(obj))
