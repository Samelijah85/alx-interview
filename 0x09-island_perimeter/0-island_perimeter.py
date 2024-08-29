#!/usr/bin/python3
"""
Module 0-island_perimeter

Contains the function island_perimeter
"""


def island_perimeter(grid):
    """Calculates the perimeter of an island in a given grid."""
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
