#!/usr/bin/python3
"""module for island perimeter"""


def island_perimeter(grid):
    """take an 2 by 2 matrix and return the perimiter
    assumption is each 1 has an sides of 1
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # 1 * 4

                # Check neighboring cells
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Subtract 2 if vertical cell is also land
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Subtract 2 if left cell is also land

    return perimeter
