"""
The robot is on m x n grid. The robot is initially located at the top-left corner. The robot tries to move to the bottom-right corner.
The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        aboveRow = [1] * n

        for _ in range(m - 1):
            currentRow = [1] * n
            for i in range(1, n):
                currentRow[i] = currentRow[i-1] + aboveRow[i]

            aboveRow = currentRow

        return aboveRow[-1]