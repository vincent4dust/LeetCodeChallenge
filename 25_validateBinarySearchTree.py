"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST)
A valid BST is defined as follows:
- the left subtree of a node contains only nodes with keys less than the node's key
- the right subtree of a node contains only nodes with keys greater than the node's key
- both the left and right subtrees must also be binary search trees
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bst(root, min_val=float('-inf'), max_val=float('inf')):
            if root == None:
                return True

            if not (min_val < root.val < max_val):
                return False

            return bst(root.left, min_val, root.val) and bst(root.right, root.val, max_val)
        
        return bst(root)