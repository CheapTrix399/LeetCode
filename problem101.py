# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_left(self,root):
        if(root == None):
            return [None]
        else:
            return [root.val] + self.get_left(root.left) + self.get_left(root.right)
    def get_right(self,root):
        if(root == None):
            return [None]
        else:
            return [root.val] + self.get_right(root.right) + self.get_right(root.left)
    def isSymmetric(self, root) -> bool:
        if(root == None):
            return True
        else:
            if(self.get_left(root.left)==self.get_right(root.right)):
                return True
            else:
                return False