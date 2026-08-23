class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        par=[i for i in range(n)]

        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]

        for n1, n2 in edges:
            p1,p2=find(n1),find(n2)
            if p1==p2:
                return False
            par[p1]=p2
            n -= 1
        return n == 1