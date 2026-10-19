class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        mat=[[0]*n for i in range(n)]
        top=0
        bottom=n-1
        left=0
        right=n-1
        num=1
        while top<=bottom and left<=right:
            #Top row: left-> right
            for col in range(left,right+1):
                mat[top][col]=num
                num+=1
            top+=1
            #Right column top->bottom
            for row in range(top,bottom+1):
                mat[row][right]=num
                num+=1
            right-=1
            #Bottom row : right->left,only if a row remains
            if top<=bottom:
                for col in range(right,left-1,-1):
                    mat[bottom][col]=num
                    num+=1
                bottom-=1
            #left column: bottom->top,only if a column remains
            if left<=right:
                for row in range(bottom,top-1,-1):
                    mat[row][left]=num
                    num+=1
                left+=1
        return mat
