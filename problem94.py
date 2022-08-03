# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        if(root == None):
            return []
        if((root.left == None)&(root.right==None)):
            return [root.val]
        else:
            if(root.left == None):
                return [root.val] + self.inorderTraversal(root.right)
            elif(root.right == None):
                return self.inorderTraversal(root.left) + [root.val]
            else:
                return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)