class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        hp={}
        
        def dfs(node):
            if node in hp:
                return hp[node]

            clone=Node(node.val)
            hp[node]=clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)