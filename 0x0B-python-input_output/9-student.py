#!/usr/bin/python3

"""Defines a class Student."""

class Student:
    """class Representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initialises a new Student.
        Args:
            first_name (str): Firstname of the student.
            last_name (str): Lastname of the student.
            age (int): age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets a dictionary representation of the Student class."""
        return self.age
