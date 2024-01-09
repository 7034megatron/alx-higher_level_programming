#!/usr/bin/python3

"""Defines a JSON file-writing function not as string."""
import json

def save_to_json_file(my_obj, filename):
    """Write into a text file using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
