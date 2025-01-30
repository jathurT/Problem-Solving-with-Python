# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Approach 1 - Recursive Approach
# class Solution(object):
#     def countNodes(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: int
#         """
#         if not root:
#             return 0
#         return 1 + self.countNodes(root.left) + self.countNodes(root.right)

class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        left_height = self.get_left_height(root.left)
        right_height = self.get_right_height(root.right)
        if left_height == right_height:
            return (1 << left_height) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def get_left_height(self, left):
        height = 0
        while left:
            height += 1
            left = left.left
        return height

    def get_right_height(self, right):
        height = 0
        while right:
            height += 1
            right = right.right
        return height
