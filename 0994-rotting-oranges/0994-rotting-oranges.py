class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        q=[]
        hasFresh=False
        l1=len(grid)
        l2=len(grid[0])
        for i in range(l1):
            for j in range(l2):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    hasFresh=True
        if not hasFresh:
            return 0
        t=0
        while len(q)>0:
            added=False
            print(q)
            newq=[]
            for i in range(len(q)):
                c=q.pop()
                i=c[0]
                j=c[1]
                if i+1<l1 and grid[i+1][j]==1:
                    grid[i+1][j]=2
                    newq.append((i+1,j))
                    added=True
                if j+1<l2 and grid[i][j+1]==1:
                    grid[i][j+1]=2
                    newq.append((i,j+1))
                    added=True
                if j-1>=0 and grid[i][j-1]==1:
                    grid[i][j-1]=2
                    newq.append((i,j-1))
                    added=True
                if i-1>=0 and grid[i-1][j]==1:
                    grid[i-1][j]=2
                    newq.append((i-1,j))
                    added =True
            q.extend(newq)
            if not added:break
            t+=1
        print(grid)
        for i in range(l1):
            for j in range(l2):
                if grid[i][j]==1:
                    return -1
        return t