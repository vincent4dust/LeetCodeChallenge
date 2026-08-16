"""
Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root: return ''
        tree = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                tree.append(str(node.val))
                queue.extend([node.left, node.right])
            else:
                tree.append('*')
        return ','.join(tree)
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data: return None
        tree = deque(data.split(','))
        root = TreeNode(int(tree.popleft()))
        queue = deque([root])
        while queue:
            node = queue.popleft()
            
            if (left := tree.popleft()) != '*':
                node.left = TreeNode(int(left))
                queue.append(node.left)
            
            if (right := tree.popleft()) != '*':
                node.right = TreeNode(int(right))
                queue.append(node.right)
                
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans