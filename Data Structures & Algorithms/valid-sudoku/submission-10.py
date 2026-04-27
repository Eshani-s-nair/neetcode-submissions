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
            count=0
            for z in range(3):
                submat=[]
                for i in range(k,3+k):
                    for j in range(z*3,3+z*3):
                        if board[i][j]!=".":
                            submat.append(board[i][j])
                x=set(submat)
                if len(submat)==len(x):
                    count+=1
                else:
                    return False
            if count !=3:
                return False
            
        return True
            

                


            
            

        







        