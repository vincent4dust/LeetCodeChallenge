"""
There is an integer array, nums in sorted in ascending order (distinct values)
Prior to being passed to function, nums is possibly rotated at an unknown pivot index k
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, 
or -1 if it is not in nums
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        mid = end / 2
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            
            if nums[start] <= nums[mid]:
                if target >= nums[start] and target <= nums[mid]:
                    end = mid -1
                else:
                    start = mid + 1
            else:
                if target >= nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            
        return -1