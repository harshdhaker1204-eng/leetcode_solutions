class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj=[[] for _ in range(numCourses)]
        # Indegree of each course
        indegree=[0]*numCourses
        #Build graph
        for course,prerequisite in prerequisites:
            adj[prerequisite].append(course)
            indegree[course]+=1
        #put courses with no prerequisites into queue
        queue=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        answer=[]
        while queue:
            current=queue.popleft()
            answer.append(current)
            #Remove current course from graph
            for next_course in adj[current]:
                indegree[next_course]-=1
                #no more prerequisites
                if indegree[next_course]==0:
                    queue.append(next_course)
        if len(answer)==numCourses:
            return answer
        return []