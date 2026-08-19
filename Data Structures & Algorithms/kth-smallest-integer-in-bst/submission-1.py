class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n=0
        stk=[]
        curr=root

        while curr or stk:
            while curr:
                stk.append(curr)
                curr=curr.left

            curr=stk.pop()
            n+=1
            if n==k:
                return curr.val
            
            curr=curr.right