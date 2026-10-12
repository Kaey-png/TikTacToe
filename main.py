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
        for j in range(3):
            if (board[i][j] == empty):
                possibleactions.append((i, j))
    
    return possibleactions

def result(board, action):
    if action == None:
        return
    
    copiedBoard = copy.deepcopy(board)
    i, j = action
    count_x = sum(row.count(X) for rows in board)
    count_o = sum(row.count(O) for rows in board)
    
    copiedBoard[i][j] = player(board)
        
    return copiedBoard

def winner(board):
    xCount = 0
    oCount = 0
    
    for row in board:
        xCount = row.count("X")
        oCount = row.count("Y")
        
    if xCount == 3:
        return X
    elif oCount == 3:
        return O

    xCount = 0
    oCount = 0
    for i in range(3):
        for j in range(3):
            if board[j][i] == X:
                xCount += 1
            elif board[j][i] == Y:
                oCount += 1

            if xCount == 3:
                return X
            elif oCount == 3:
                return O
        xCount = 0
        oCount = 0
    
    xCount = 0
    oCount = 0  
    
    diagonal1 = [board[0][0], board[1][1], board[2][2]]
    diagonal2 = [board[0][2], board[1][1], board[2][0]]
    
    xCount = diagonal1.count("X")
    oCount = diagonal1.count("O")
    
    if xCount == 3:
        return X
    elif oCount == 3:
        return O
    
    xCount = diagonal2.count("X")
    oCount = diagonal2.count("X")
    
    if xCount == 3:
        return X
    elif oCount == 3:
        return O
    
    
    xCount = 0
    oCount = 0
    

def terminal(board):
    utilityVal = utility(board)
    emptyCount = sum(row.count(empty) for row in board)
    if utilityVal == 1:
        return True
    elif utilityVal == -1:
        return True
    elif emptyCount == 0:
        return True
    else:
        return False
    
def utility(board):
    winnerofMatch = winner(board)
    
    if winnerofMatch == "X":
        return 1
    elif winnerofMatch == "O":
        return -1
    else:
        return 0

def minimax(board):
    possibleActions = actions(board)
    copiedBoard = copy.deepcopy(board)
    
    if currentPlayer == 'X':
        v = float('-inf')
        toBeAction = None
        
        for action in possibleActions:
            resultByAction = result(copiedBoard, action)
            value = minValue(resultByAction)
            if value < v:
                v = value
                toBeAction = action
        return toBeAction

def maxValue(board):
    if terminal(board):
        return utility(board)
    v = float('-inf')
    for action in actions(board):
        v = max(v, minValue(result(board, action))) 
    return v

def minValue(board):
    if terminal(board):
        return utility(board)
    v = float('-inf')
    for action in actions(board):
        v = max(vmaxValue(result(board, action)))   
    
