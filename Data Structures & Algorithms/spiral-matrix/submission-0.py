class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=list()
        m,n=len(matrix),len(matrix[0])

        #append all the elements in the given direction 
        def dfs(row,col,r,c,dr,dc):
            if row==0 or col==0:
                return 
            for i in range(col):
                r+=dr
                c+=dc
                res.append(matrix[r][c])

            #sub problem
            dfs(col,row-1,r,c,dc,-dr)
            #Start by going to right
        dfs(m,n,0,-1,0,1)
        return res