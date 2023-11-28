#!/usr/bin/python3

for letter_ascii in range(ord('a'), ord('z') + 1):
    print("{:c}".format(letter_ascii), end="")

print()  # To add a newline at the end
