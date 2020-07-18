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
    empty_count = 0
    for lst in board:
        empty_count += lst.count(EMPTY)
    return X if empty_count % 2 == 1 else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    allowed_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                allowed_actions.add((i,j))

    # Specification says return anything when empty
    if len(allowed_actions) == 0:
        allowed_actions.add((1,1))

    return allowed_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row = action[0]
    col = action[1]
    if board[row][col] != EMPTY:
        raise AssertionError

    new_board = copy.deepcopy(board)
    new_board[row][col] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    def has_won(board, user):
        for ind in range(3):
            if board[ind][0] == user and board[ind][1] == user and board[ind][2] == user:
                return True
            if board[0][ind] == user and board[1][ind] == user and board[2][ind] == user:
                return True
        if board[0][0] == user and board[1][1] == user and board[2][2] == user:
            return True
        if board[0][2] == user and board[1][1] == user and board[2][0] == user:
            return True
        return False

    if has_won(board, X):
        return X
    elif has_won(board, O):
        return O
    else:
        return None
        

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    the_winner = winner(board)
    if the_winner == X:
        return 1
    elif the_winner == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board):
        """
        Determine max value with given board.
        """
        if terminal(board):
            return utility(board)

        # 1, 0, -1 are only allowed values, so -2 can act as -ve infinity
        max_val = -2
        for action in actions(board):
            max_val = max(max_val, min_value(result(board, action)))

            # Not needed, but can improves performance
            if max_val == 1:
                break
        return max_val

    def min_value(board):
        """
        Determine min value with given board.
        """
        if terminal(board):
            return utility(board)

        # 1, 0, -1 are only allowed values, so 2 can act as +ve infinity
        min_val = 2
        for action in actions(board):
            min_val = min(min_val, max_value(result(board, action)))

            # Not needed, but can improves performance
            if min_val == -1:
                break
        return min_val

    # Search for optimal value - which depends if playing X or O.
    optimal_action = None
    to_play = player(board)
    if to_play == X:
        max_val = -2
        for action in actions(board):
            value = min_value(result(board, action))
            if value > max_val:
                max_val = value
                optimal_action = action

                # Not needed, but can improves performance
                if max_val == 1:
                    break
    else:
        min_val = 2
        for action in actions(board):
            value = max_value(result(board, action))
            if value < min_val:
                min_val = value
                optimal_action = action

                # Not needed, but improves performance
                if min_val == -1:
                    break

    return optimal_action
