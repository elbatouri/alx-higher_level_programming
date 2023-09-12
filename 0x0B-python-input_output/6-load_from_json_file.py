#!/usr/bin/python3
"""Defines a function that is a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Create from a JSON file a Python object."""
    with open(filename) as f:
        return json.load(f)
