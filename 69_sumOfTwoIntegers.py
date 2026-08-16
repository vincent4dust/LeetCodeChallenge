"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.
"""

class Solution:
    def getSum(self, a: int, b: int) -> int:
        max_int, mask = 0x7FFFFFFF, 0xFFFFFFFF
        
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        return a if a <= max_int else ~(a ^ mask)