import math

def print_board(board):
    for line in board:
        print(line)


def check(board,row,col,num):
    for r in range(len(board)):
        if r == row:
            continue
        if num == board[r][col]:
            return False
    for c in range(len(board[0])):
        if c == col:
            continue
        if num == board[row][c]:
            return False
    len_sq = round(math.sqrt(len(board)))
    start = [row-(row%len_sq),col-(col%len_sq)]
    for r in range(start[0],start[0]+len_sq):
        for c in range(start[1],start[1]+len_sq):
            if num == board[r][c]:
                return False
    return True

def fun(board):
    n = len(board)
    row = -1
    col = -1
    empty = False
    for r in range(n):
        for c in range(n):
            if not empty and board[r][c] == 0:
                row = r
                col = c
                empty = True
                break
        if empty:
            break
    if not empty:
        print_board(board)
        return True

    for i in range(1,n+1):
        if check(board,row,col,i):
            board[row][col] = i
            if fun(board):
                return True
            else:
                board[row][col] = 0
    return False

if __name__ == '__main__':
    board = [[0 for i in range(9)] for j in range(9)]
    print(fun((board)))

