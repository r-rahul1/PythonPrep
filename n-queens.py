'''
N-Queens- python solution
n -> n creates n*n board
'''
n = 4
board = [['.' for i in range(n)] for j in range(n)]

def print_board(board):
    for b in board:
        print('|',end=' ')
        for element in b:
            if element == '.':
                print('.', end=' ')
            else:
                print('Q', end=' ')
        print('|')
    print()

def check(board,r,c,n):
    for row in range(0, n):
        if board[row][c] == 'Q':
            return False
    for col in range(0, n):
        if board[r][col] == 'Q':
            return False
    row, col = r - 1, c - 1
    while row >= 0 and col >= 0:
        if board[row][col] == 'Q':
            return False
        row -= 1
        col -= 1
    row, col = r - 1, c + 1
    while row >= 0 and col < n:
        if board[row][col] == 'Q':
            return False
        row -= 1
        col += 1
    return True

def fun(board,r,n):
    if r == n:
        #for b in board:
        #    print(b)
        #print()
        print_board(board)
        return 1
    count = 0
    for c in range(0,n):
        if not board[r][c]:
            continue
        if check(board,r,c,n):
            board[r][c] = 'Q'
            count += fun(board,r+1,n)
            board[r][c] = '.'
    return count

print(fun(board,0,n))