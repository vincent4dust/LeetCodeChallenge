"""
Given an mxn integer matrix, if an element is 0,
set its entire row and column to 0
"""

# space complexity O(m + n)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        zeroes_row = [False] * m
        zeroes_col = [False] * n
 
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zeroes_row[row] = True
                    zeroes_col[col] = True

        for row in range(m):
            for col in range(n):
                if zeroes_row[row] == True or zeroes_col[col] == True:
                    matrix[row][col] = 0