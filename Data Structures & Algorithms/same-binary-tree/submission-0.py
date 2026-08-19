class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        
        s1=[p]
        s2=[q]

        while s1 and s1:
            c1=s1.pop()
            c2=s2.pop()
            if c1 is None and c2 is None:
                continue
            if c1 is None or c2 is None:
                return False
            if c1.val!=c2.val:
                return False
            
            s1.append(c1.left)
            s1.append(c1.right)
            s2.append(c2.left)
            s2.append(c2.right)

        return True

            

