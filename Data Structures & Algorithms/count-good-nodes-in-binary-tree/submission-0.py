class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,maxval):
            if root is None:
                return 0
            good=1 if root.val>=maxval else 0

            maxval=max(maxval,root.val)
    
            return good+dfs(root.left,maxval)+dfs(root.right,maxval)
        
        return dfs(root,root.val)