class Solution:
    def binary_search(self,row:List[int],target:int)->bool:
        left=0
        right=len(row)-1
        while left<=right:
            middle=(left+right)//2
            if target==row[middle]:
                return True
            if target<row[middle]:
                right=middle-1
            if target>row[middle]:
                left=middle+1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_r=len(matrix)
        n_c=len(matrix[0])
        first_row=0
        last_row=n_r-1
        
        while first_row<=last_row:
            middle_row=(first_row+last_row)//2
            if target<matrix[middle_row][0]:
                last_row=middle_row-1
            elif target>matrix[middle_row][n_c-1]:
                first_row=middle_row+1
            else:
                return self.binary_search(matrix[middle_row],target)
        return False