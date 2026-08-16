"""
Given an mxn matrix, return all elements of the matrix in spiral order
"""

# the intuition is always remove first row from matrix
# tranpose the matrix, and reversed order of matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        sol = []
        while matrix:
            sol += matrix.pop(0)
            matrix = (list(zip(*matrix)))[::-1]

        return sol