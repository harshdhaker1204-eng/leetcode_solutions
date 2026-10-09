class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        if len(connections)<n-1:
            return -1
        adj=[[] for _ in range(n)]
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
        visited=set()
        components=0
        def dfs(node):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
        for i in range(n):
            if i not in visited:
                dfs(i)
                components+=1
        return components-1