# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def Checker (p,q):
            if p == None  and q==None : return True
            if (p!=None and q==None) or (p==None and q!=None): return False
            return p.val==q.val and Checker (p.left,q.right)and Checker (p.right,q.left)
        return Checker(root,root)
        