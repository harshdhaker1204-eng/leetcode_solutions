class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n=len(graph)
        color=[-1]*n
        for start in range(n):
            if color[start]!=-1:
                continue
            q=deque([start])
            color[start]=0
            while q:
                node=q.popleft()
                for neighbor in graph[node]:
                    if color[neighbor]==-1:
                        color[neighbor]=1-color[node]
                        q.append(neighbor)
                    elif color[neighbor]==color[node]:
                        return False
        return True