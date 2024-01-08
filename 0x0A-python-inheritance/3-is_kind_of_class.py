#!/usr/bin/python3

"""Defines a class that has inherited class-checking method."""


def is_kind_of_class(obj, a_class):
    """Check if an object is inherited or an instance of a class.
    Args:
        obj (any): The object to be  checked.
        a_class (type): The class to be matched to the type of boject.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
