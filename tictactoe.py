"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    Xcount = 0
    Ocount = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == X:
                Xcount += 1
            if board[row][col] == O:
                Ocount += 1
    if Xcount>Ocount:
        return O
    else:
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    PossibleActions = set()
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                PossibleActions.add((row, col))
    return PossibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception('Invalid move')
    row, col = action
    copy_board = copy.deepcopy(board)
    copy_board[row][col] = player(board)
    return copy_board

def checkWinner(board, player):
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    for col in range(len(board)):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    if board[1][1] == player:
        if (board[0][0] == player and board[2][2] == player) or (board[0][2] == player and board[2][0] == player):
            return True
    return False

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkWinner(board, X):
        return X
    elif checkWinner(board, O):
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X:
        return True
    if winner(board) == O:
        return True
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
 
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board) == X:
        moves = []
        for action in actions(board):
            moves.append([min_value(result(board, action)), action])
        return sorted(moves, key = lambda x: x[0], reverse = True)[0][1]
    elif player(board) == O:
        moves = []
        for action in actions(board):
            moves.append([max_value(result(board, action)), action])
        return sorted(moves, key = lambda x: x[0])[0][1]

