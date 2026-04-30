class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res=[]
        def preorder(root):
            nonlocal res
            res = []
            return preorder_recursive(root)
        
        def preorder_recursive(root):
            if root is not None:
                res.append(root)
                preorder_recursive(root.left)
                preorder_recursive(root.right)
            return res

        def isSameTree(p, q):
            if not p and not q: return True
            if not p or not q: return False
            return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        x=preorder(root)
        y=preorder(subRoot)
        
        for node in x:
            if isSameTree(node, subRoot):
                return True
        return False