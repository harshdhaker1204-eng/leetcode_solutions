class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)

        visited = [False] * n
        minDist = [float("inf")] * n

        minDist[0] = 0
        total_cost = 0

        for _ in range(n):
            # Find the unvisited point with minimum distance
            u = -1

            for i in range(n):
                if not visited[i] and (u == -1 or minDist[i] < minDist[u]):
                    u = i

            # Add this point to MST
            visited[u] = True
            total_cost += minDist[u]

            # Update distances of remaining points
            for v in range(n):
                if not visited[v]:
                    x1, y1 = points[u]
                    x2, y2 = points[v]

                    cost = abs(x1 - x2) + abs(y1 - y2)

                    minDist[v] = min(minDist[v], cost)

        return total_cost