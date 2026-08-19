from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=deque([root])
        out=[]
        while queue:
            level=[]
            levlen=len(queue)

            for i in range(levlen):
                curr=queue.popleft()
                level.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            out.append(level)
            
        
        return out
