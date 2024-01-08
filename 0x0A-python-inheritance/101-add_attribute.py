#!/usr/bin/python3

"""This is a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object.
    Args:
        obj (any): The object we will add attribute to.
        att (str): The name of the attribute we will add to the object.
        value (any): The value of attribute.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
