class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}

        for src, dst in tickets:
            if src not in adj:
                adj[src] = []
            adj[src].append(dst)

        for src in adj:
            adj[src].sort(reverse=True)

        res = []

        def dfs(src):
            while adj.get(src):
                dst = adj[src].pop()
                dfs(dst)

            res.append(src)

        dfs("JFK")
        return res[::-1]