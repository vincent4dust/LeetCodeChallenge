"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.dfs(root, subRoot)
        
    def dfs(self, root, subRoot):
        if root == None:
            return False

        if subRoot == None:
            return True

        if self.similar(root, subRoot):
            return True

        return self.dfs(root.left, subRoot) or self.dfs(root.right, subRoot)

    def similar(self, r, s):
        if r == None and s == None:
            return True

        if r and s and r.val == s.val:
            return self.similar(r.left, s.left) and self.similar(r.right, s.right)

        return False