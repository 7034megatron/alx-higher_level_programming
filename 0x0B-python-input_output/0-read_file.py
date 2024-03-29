#!/usr/bin/python3

"""
Module for reading a text file (UTF8) and printing it to stdout.
"""

def read_file(filename=""):
    """
    Function that reads a text file (UTF8) and prints it to stdout.
    Args:
        filename (str): The name of the file to be read.
    Returns:
        None
    """
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end='')

if __name__ == "__main__":
    read_file("my_file_0.txt")
