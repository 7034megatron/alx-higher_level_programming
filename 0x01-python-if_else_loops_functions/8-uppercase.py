#!/usr/bin/python3

def uppercase(s):
    for char in s:
        upper_char = char
        if ord('a') <= ord(char) <= ord('z'):
            upper_char = chr(ord(char) - ord('a') + ord('A'))
        print("{}".format(upper_char), end="")
    print("")
