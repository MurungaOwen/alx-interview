#!/usr/bin/python3
"""
rotating a 2d matrix
"""


def rotate_2d_matrix(matrix) -> None:
    """rotate matrix 90 degrees clockwise"""
    N = len(matrix[0])
    cycles = N // 2
    for i in range(cycles):
        for j in range(i, N - i - 1):
            first = matrix[i][j]
            matrix[i][j] = matrix[N - 1 - j][i]
            matrix[N - 1 - j][i] = matrix[N - 1 - i][N - 1 - j]
            matrix[N - 1 - i][N - 1 - j] = matrix[j][N - 1 - i]
            matrix[j][N - 1 - i] = first
