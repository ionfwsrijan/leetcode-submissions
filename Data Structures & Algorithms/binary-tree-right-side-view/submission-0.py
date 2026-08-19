from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        out=[]
        queue=deque([root])

        while queue:
            rightSide=None
            levlen=len(queue)

            for i in range(levlen):
                curr=queue.popleft()
                if curr:
                    rightSide=curr
                    queue.append(curr.left)
                    queue.append(curr.right)

            if rightSide:
                out.append(rightSide.val)
        
        return out
