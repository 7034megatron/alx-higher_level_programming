#!/usr/bin/python3

"""Defines a class that is used to check a function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.
    Args:
        obj: The object to check.
        a_class: The class to match to the type of object.
    Returns:
        If obj is the same as the instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
