# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def check(node):
            if not node:
                return 1

            check_left=check(node.left)
            if check_left==-1:
                return -1
            
            check_right=check(node.right)
            if check_right==-1:
                return -1

            if abs(check_left-check_right)>1:
                return -1

            return 1+max(check_left,check_right)

        return check(root)>=1
            


            
            
        
        