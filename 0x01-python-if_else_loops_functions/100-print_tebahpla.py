#!/usr/bin/python3

for c in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format(c) + "{:c}".format(c - 32), end="")
