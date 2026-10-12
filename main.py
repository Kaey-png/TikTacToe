import copy

X = "X"
O = "O"
empty = None


def initialState():
    return [[empty] * 3 for _ in range(3)]


def player(board):
    count_x = sum(row.count(X) for row in board)
    count_o = sum(row.count(O) for row in board)
    return O if count_x > count_o else X


def actions(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == empty]


def result(board, action):
    if action is None:
        return None
    newBoard = copy.deepcopy(board)
    i, j = action
    newBoard[i][j] = player(board)
    return newBoard


def winner(board):
    lines = []
    lines.extend(board)                                            # rows
    lines.extend([board[0][c], board[1][c], board[2][c]] for c in range(3))  # columns
    lines.append([board[0][0], board[1][1], board[2][2]])          # diagonal 1
    lines.append([board[0][2], board[1][1], board[2][0]])          # diagonal 2

    for line in lines:
        if line.count(X) == 3:
            return X
        if line.count(O) == 3:
            return O
    return None


def utility(board):
    w = winner(board)
    if w == X:
        return 1
    if w == O:
        return -1
    return 0


def terminal(board):
    return winner(board) is not None or all(cell != empty for row in board for cell in row)


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
    v = float('inf')
    for action in actions(board):
        v = min(v, maxValue(result(board, action)))
    return v


def minimax(board):
    if terminal(board):
        return None

    bestAction = None
    if player(board) == X:
        v = float('-inf')
        for action in actions(board):
            value = minValue(result(board, action))
            if value > v:
                v = value
                bestAction = action
    else:
        v = float('inf')
        for action in actions(board):
            value = maxValue(result(board, action))
            if value < v:
                v = value
                bestAction = action
    return bestAction