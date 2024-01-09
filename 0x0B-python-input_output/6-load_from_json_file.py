#!/usr/bin/python3

"""This defines a JSON file-reading function not a string."""
import json

def load_from_json_file(filename):
    """Create a Python reading  from a JSON file."""
    with open(filename) as f:
        return json.load(f)
