#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """A function that returns a list of integers"""
    if n <= 0:
        return []

    # Intialize pascal's triangle with the first row
    triangle = [[1]]

    # Generate other rows
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        row.append(1)
        triangle.append(row)

    return triangle