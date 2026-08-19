class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia=0
        def dfs(node):
            nonlocal dia
            if not node:
                return 0
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)
            dia= max(dia,leftHeight+rightHeight)
            return 1+max(leftHeight,rightHeight)

        dfs(root)

        return dia