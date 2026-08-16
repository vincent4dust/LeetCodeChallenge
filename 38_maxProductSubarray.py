"""
Given an integer array nums, find a 
subarray that has the largest product, and return the product.
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        smallest, largest = 1, 1
        res = nums[0]

        for n in nums:
            vals = (n, n*smallest, n*largest)
            smallest, largest = min(vals), max(vals)

            res = max(res, largest)

        return res