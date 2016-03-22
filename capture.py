# Check program to see if piece(s) can be captured
# Array Code Conventions
# 0 - No Stone
# 1 - Black Stone
# 2 - White Stone

def main(board, piece1):
    ''' Main Function'''
    piece2 = getOpponent(piece1) 
    for x in range(0, len(board)):
        for y in range(0, len(board[x])):
            if (board[x][y] == piece2):
                checkCaptures(board, x, y, piece1)

    printBoard(board)

def getOpponent(player):
    if (player == 1):
        return 2
    else:
        return 1

def checkCaptures(board, x, y, player):
    opp = board[x][y] # Enemy color
    n = 0
    
    # Check liberties
    n = evaluateLib(board, x, y, n, player, opp)
    if (n == -4):
        board[x][y] = 0

def evaluateLib(board, x, y, n, player, opp):
    if (board[x][y+1] == player):
        n -= 1
    elif (board[x][y+1] == opp):
        n = evaluateLib(board, x, y+1, n, player, opp)

    if (board[x][y-1] == player):
        n -= 1
    elif (board[x][y-1] == opp):
        n = evaluateLib(board, x, y-1, n, player, opp)

    if (board[x-1][y] == player):
        n -= 1
    elif (board[x-1][y] == opp):
        n = evaluateLib(board, x-1, y, n, player, opp)

    if (board[x+1][y] == player):
        n -= 1
    elif (board[x+1][y] == opp):
        n = evaluateLib(board, x+1, y, n, player, opp)

    return n

def printBoard(board):
    for row in board:
        print(row)

main([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ], 2)
