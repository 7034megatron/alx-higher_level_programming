#!/usr/bin/python3

for letter_ascii in range(ord('a'), ord('z') + 1):
    if chr(letter_ascii) not in {'q', 'e'}:
        print("{:c}".format(letter_ascii), end="")
