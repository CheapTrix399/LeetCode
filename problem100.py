# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_inorder(self, p):
        if(p == None):
            return [None]
        if((p.left == None)&(p.right==None)):
            return [p.val]
        else:
            return  [p.val] + self.get_inorder(p.left) + self.get_inorder(p.right)
    def isSameTree(self, p, q):
        if(self.get_inorder(p)==self.get_inorder(q)):
            return True
        else:
            return False