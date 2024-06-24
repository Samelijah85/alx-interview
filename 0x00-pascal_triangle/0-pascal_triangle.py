#!/usr/bin/python3
"""0-pascal_triangle"""


def pascal_triangle(n):
    """
    Pascal's Triangle
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(n - 1):
        row = [1]
        for j in range(len(triangle[-1]) - 1):
            row.append(triangle[-1][j] + triangle[-1][j + 1])
        row.append(1)
        triangle.append(row)
    return triangle
