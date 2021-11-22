# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        checker =[]
        sum=0
        def sumnode(node,sum):
            if node==None :return 0
            if node!=None:
                if node.left==None and node.right==None : 
                    sum+=node.val
                    checker.append(sum)
                else:
                    sum+=node.val
                sumnode(node.left,sum)
                sumnode(node.right,sum)
                

        sumnode(root,0)
        if targetSum in checker : return True
                


            