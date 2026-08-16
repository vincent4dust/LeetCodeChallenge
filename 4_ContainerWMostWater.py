# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         n = len(height)
#         maxV = -1
#         for i in range(n):
#             for j in range(i+1, n):
#                 tempV = (j-i) * min(height[i], height[j])
#                 if tempV > maxV:
#                     maxV = tempV
        
#         return maxV

"""
O(n^2) - quadratic time complexity
We want to maintain the max height between 2 endpoints
Therefore, iterate only of of the endpoint
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        left = 0
        right = len(height) - 1

        while left < right:
            maxArea = max(maxArea, ((right - left) * (min(height[left], height[right]))))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxArea