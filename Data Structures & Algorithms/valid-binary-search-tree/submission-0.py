class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root,lb,rb):
            if not root:
                return True
            if not (root.val>lb and root.val<rb):
                return False
            return (valid(root.left,lb,root.val) and valid(root.right,root.val,rb))

        return valid(root,float('-inf'),float('inf'))