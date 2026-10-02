from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        graph = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[b].append(a)

        indegree = [0] * numCourses

        for a, b in prerequisites:
            indegree[a] += 1

        queue = deque()

        # Add courses with no prerequisites
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        completed = 0

        while queue:

            # Remove one course
            current = queue.popleft()

            completed += 1

            # Process courses dependent on current
            for next_course in graph[current]:

                # One prerequisite is completed
                indegree[next_course] -= 1

                # No prerequisites remain
                if indegree[next_course] == 0:
                    queue.append(next_course)

        return completed == numCourses
