"""
Tic Tac Toe Player
"""

import math
import copy

from numpy import true_divide

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
    #    Returns player who has the next turn on a board.
    #   let O chance is first
    countX = 0
    countO = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X":
                countX = countX + 1
            elif board[i][j] == "O":
                countO = countO + 1

    if countX == 0 and countO == 0:
        return "O"

    if countX == countO:
        return "O"
    elif countX > countO:
        return "O"
    else:
        return "X"


def actions(board):

    #   Returns set of all possible actions (i, j) available on the board.

    possible_actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                possible_actions.append([i, j])

    return possible_actions


def result(board, action):

    # Returns the board that results from making move (i, j) on the board.
    result = copy.deepcopy(board)
    result[action[0]][action[1]] = player(board)
    return result


def winner(board):
    #   Returns the winner of the game, if there is one.

    checkPos = [[[0, 0], [0, 1], [0, 2]], [[1, 0], [1, 1], [1, 2]], [[2, 0], [2, 1], [2, 2]], [[0, 0], [1, 0], [
        2, 0]], [[0, 1], [1, 1], [2, 1]], [[0, 2], [1, 2], [2, 2]], [[0, 0], [1, 1], [2, 2]], [[0, 2], [1, 1], [2, 0]]]

    for position in checkPos:
        threeX = 0
        threeO = 0
        for i in range(3):
            if board[position[i][0]][position[i][1]] == "X":
                threeX = threeX+1
            elif board[position[i][0]][position[i][1]] == "O":
                threeO = threeO+1
            if threeO == 3:
                return "O"
            elif threeX == 3:
                return "X"
    return None


def terminal(board):

    # Returns True if game is over, False otherwise.
    if winner(board) != None:
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                return False

    return True


def utility(board):

    # Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0


def minimax(board):
    # Returns the optimal action for the current player on the board.
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move


def max_value(board):
    if terminal(board):
        return utility(board), None

    # v = float('-inf')
    v = -100
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = min_value(result(board, action))
        if aux > v:
            v = aux
            move = action
            if v == 1:
                return v, move

    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None

    # v = float('inf')
    v = 100
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = max_value(result(board, action))
        if aux < v:
            v = aux
            move = action
            if v == -1:
                return v, move

    return v, move
