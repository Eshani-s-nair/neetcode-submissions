class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                for k in range(j+1,9):
                    if board[i][j]!="." and board[i][k]!=".":
                        if board[i][j]==board[i][k]:
                            return False
        
        for j in range(9):
            for i in range(9):
                for k in range(i+1,9):
                    if board[i][j]!="." and board[k][j]!=".":
                        if board[i][j]==board[k][j]:
                            return False

        for k in range(0,9,3):
            submat1=[]
            submat2=[]
            submat3=[]
            for i in range(k,3+k):
                for j in range(0,3):
                    if board[i][j]!=".":
                        submat1.append(board[i][j])
            for i in range(k,3+k):
                for j in range(3,6):
                    if board[i][j]!=".":
                        submat2.append(board[i][j])
            for i in range(k,3+k):
                for j in range(6,9):
                    if board[i][j]!=".":
                        submat3.append(board[i][j])
            x=set(submat1)
            y=set(submat2)
            z=set(submat3)
            if len(submat1)==len(x) and len(submat2)==len(y):
                if len(submat3)==len(z):
                    continue
            else:
                return False
            
        return True
            

                


            
            

        







        