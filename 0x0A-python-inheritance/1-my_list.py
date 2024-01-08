#!/usr/bin/python3

"""This is a child class of the list class"""

class MyList(list):
    """The is the class definition of the child class MYLIST"""

    def print_sorted(self):
        """This is the method for print sorted definition"""
        print(sorted(self))
