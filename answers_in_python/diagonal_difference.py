"""
Given a square matrix, calculate the absolute difference 
between the sums of its diagonals.

Link: https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true
"""

def diagonalDifference(arr):
    matrix = len(arr)
    sum_leading_diagonal = 0
    sum_secondary_diagonal = 0

    for i in range(matrix):
        sum_leading_diagonal += arr[i][i]
        sum_secondary_diagonal += arr[i][matrix - 1 - i]

    absolute_diagonal_difference = abs(sum_leading_diagonal - sum_secondary_diagonal)

    return absolute_diagonal_difference
