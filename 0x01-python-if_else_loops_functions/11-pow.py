#!/usr/bin/python3

def pow(a, b):
    result = 1
    tolerance = 1e-15  # Adjust this value based on your precision requirements

    if b < 0:
        a = 1 / a
        b = abs(b)

    for _ in range(b):
        result *= a

    if abs(result - round(result)) < tolerance:
        result = round(result)

    return result
