class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        parent=[i for i in range(len(edges)+1)]
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x]) #path compression
            return parent[x]
        def union(x,y):
            px,py=find(x),find(y)
            if px==py:
                return False #cycle found
            parent[px]=py
            return True
        for u,v in edges:
            if not union(u,v):
                return [u,v]
        