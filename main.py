import math
import copy

print("------------------Tic Tak Toe---------------------")
print("O-------X")

X = "X"
O = "O"
empty = None

def initialState():
    return [
        [empty, empty, empty],
        [empty, empty, empty],
        [empty, empty, empty]
    ]

def player(board):
    count_x = sum(row.count(X) for rows in board)
    count_o = sum(row.count(O) for rows in board)
    
    
    if count_x > count_o:
        value = "O"
        
    else:
        value = "X"
    
    return value

def actions(board):
    possibleactions = []
    
    for i in range(3):
        for j in range(3)
    if (board[i][j] == empty):
        possibleactions.append((i, j))
    
    return possible actions

def result(board, action):
    if action = None:
        return
    
    copiedBoard = copy.deepcopy(board)
    i, j = action
    count_x = sum(row.count(X) for rows in board)
    count_o = sum(row.count(O) for rows in board)
    
    copiedBoard[i][j] = player(board)
        
    return copiedBoard

    
