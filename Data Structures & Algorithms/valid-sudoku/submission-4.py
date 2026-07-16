class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for r in board:
            rdict = {}
            for num in r:
                if num.isnumeric():
                    if num in rdict:
                        return False
                    else:
                        rdict[num] = 1
        
        for c in range(9):
            cdict = {}
            for r in range(9):
                box = board[r][c]
                if box.isnumeric():
                    if box in cdict:
                        return False
                    else:
                        cdict[box] = 1

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        
        return True
        




