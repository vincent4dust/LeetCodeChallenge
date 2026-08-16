"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = [root.val]

        def DFS(root):
            if root is None:
                return 0

            lmax = DFS(root.left)
            rmax = DFS(root.right)
            # if one side is negative, no need to consider traversal
            lmax = 0 if lmax < 0 else lmax
            rmax = 0 if rmax < 0 else rmax

            maxPath[0] = max(maxPath[0], root.val + lmax + rmax)

            return root.val + max(lmax, rmax)

        DFS(root)
        return maxPath[0]