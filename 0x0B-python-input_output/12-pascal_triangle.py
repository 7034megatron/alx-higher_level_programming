#!/usr/bin/python3

"""A function that does the pascal triange"""

def pascal_triangle(n):
    """definition of a function that does the pascal"""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle

if __name__ == "__main__":
    # Test the function with the provided example
    print_triangle(pascal_triangle(5))
