#!/usr/bin/python3
"""Defines  string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a text as string object."""
    return json.dumps(my_obj)
