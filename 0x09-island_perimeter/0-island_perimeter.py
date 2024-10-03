#!/usr/bin/python3
""" a module to calculate the land perimeter of an island """


def island_perimeter(grid):
    """ A function that calculates the perimeter of an island """

    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check all four possible directions
                if r == 0 or grid[r - 1][c] == 0:  # top
                    perimeter += 1
                if r == rows - 1 or grid[r + 1][c] == 0:  # bottom
                    perimeter += 1
                if c == 0 or grid[r][c - 1] == 0:  # left
                    perimeter += 1
                if c == cols - 1 or grid[r][c + 1] == 0:  # right
                    perimeter += 1

    return perimeter
