class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Checking for repitition in rows
        for i in range(9):
            hash_row=set([])
            for j in range(9):
                if board[i][j].isdigit() and board[i][j] not in hash_row:
                    hash_row.add(board[i][j])
                elif board[i][j].isdigit() and board[i][j] in hash_row:
                    return False
        
        #Checking in a column
        for i in range(9):
            hash_col=set([])
            for j in range(9):
                if board[j][i].isdigit() and board[j][i] not in hash_col:
                    hash_col.add(board[j][i])
                elif board[j][i].isdigit() and board[j][i] in hash_col:
                    return False

        #Checking in grid
        for r in [0,3,6]:
            for c in [0,3,6]:
                seen=set([])
                for i in range(r,r+3):
                    for  j in range(c,c+3):
                        if board[i][j].isdigit() and board[i][j]not in seen:
                            seen.add(board[i][j])
                        elif board[i][j].isdigit() and board[i][j] in seen:
                            return False

        return True