#!/usr/bin/python3

"""
This program is for writing output
"""

def write_file(filename="", text=""):
    """This function writes to the standart output"""
    with open('filename', 'w', encoding="utf-8") as file:
        for line in file:
            return file.write(text)
