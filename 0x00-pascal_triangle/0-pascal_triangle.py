#!/usr/bin/python3

"""
This script contains a function code for a Pascal's Triangle.

Example:
    pascal_triangle(5)
"""

def pascal_triangle(n):
    """
    This function defines a Pascal's Triangle.

    Args: n (int): The number of rows to generate in Pascal's Triangle.

    Returns:
    list of lists: Pascal's Triangle to the nth row.
    """

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]

        for x in range(1, i):
            row.append(triangle[i-1][x-1] + triangle[i-1][x])

        row.append(1)

        triangle.append(row)

    return triangle
