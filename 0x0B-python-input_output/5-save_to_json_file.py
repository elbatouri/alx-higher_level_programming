#!/usr/bin/python3
"""Defines a fuction that is JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Write using JSON representation an object to a text file."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
