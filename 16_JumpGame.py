"""
Given an integer array nums, you are initially positioned at the array's first index,
and each element in the array represents your maximum jump lenght at that position

Return true if you can reach the last index, or false otherwise
"""

# recursive method: time limit exceeded
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def findJump(pos):
            result = False
            jump = nums[pos]

            if pos + jump >= n - 1:
                return True
            else:
                for i in range(1, jump + 1):
                    result = findJump(pos + i)
                    if result:
                        break
            
            return result

        n = len(nums)
        pos = 0
        return findJump(pos)
    

# intuition: change the destination point backwards
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # original destination is last index
        goal = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            # update the goal index
            if i + nums[i] >= goal:
                goal = i
        
        # can start from index=0
        return True if goal == 0 else False