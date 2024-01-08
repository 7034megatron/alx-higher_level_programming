#!/usr/bin/python3

"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represents base geometry."""

    def area(self):
        """if not implemented."""
        raise Exception("when area() is not implemented")
