"""
Given the root of a binary tree, return its max depth
A binary tree's max depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        def bsf(count, root):
            if root == None:
                return count
            
            count += 1

            return max(bsf(count, root.left), bsf(count, root.right))

        return bsf(count, root)