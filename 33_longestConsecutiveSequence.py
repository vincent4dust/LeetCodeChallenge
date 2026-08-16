"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = list(dict.fromkeys(nums))
        nums.sort()

        maxLength = 0
        current = 0

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1] - 1:
                current += 1
            else:
                current = 0
            if current > maxLength:
                maxLength = current

        # if maxLength > 0:
        #     return maxLength + 1
        # else:
        return maxLength + 1