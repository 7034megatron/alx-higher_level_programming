#!/usr/bin/python3

"""Defines a function that converts string-to-JSON."""
import json


def to_json_string(my_obj):
    """This function returns the JSON representation of a string object."""
    return json.dumps(my_obj)
