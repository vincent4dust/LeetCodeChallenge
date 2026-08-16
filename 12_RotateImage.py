"""
Given n x n matrix representing an image, rotate the image by 90 degrees.
"""

# matrix[::-1] reversed order matrix
# zip(*matrix[::-1]) tranpose matrix

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = zip(*matrix[::-1])