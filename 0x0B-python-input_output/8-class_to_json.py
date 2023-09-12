#!/usr/bin/python3
"""Defines a new funtion that is a Python class-to-JSON function."""


def class_to_json(obj):
    """Return the dictionary represntation of a basicly data structure."""
    return obj.__dict__
