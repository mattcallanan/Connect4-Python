import math
import random
from timeit import default_timer as timer

from agent import Agent
from board import get_valid_locations, is_terminal_node, winning_move, get_next_open_row, drop_piece
from core import PLAYER1_ID, PLAYER2_ID, COLUMN_COUNT, ROW_COUNT

EMPTY = 0
WINDOW_LENGTH = 4


# TODO: Use Player instead of piece, and "opponent" instead of "PLAYER1_ID"

class MiniMaxAgent(Agent):

    def __init__(self, params=None):
        if params is None:
            params = {}
        self.params = params

    def get_move(self, board):
        column, value = self.minimax(board, self.params['depth'], self.params['alpha'], self.params['beta'],
                                     self.params['maximizingPlayer'])
        return column

    def minimax(self, board, depth, alpha, beta, maximizingPlayer):
        valid_locations = get_valid_locations(board)
        is_terminal = is_terminal_node(board)
        if depth == 0 or is_terminal:
            if is_terminal:
                if winning_move(board, PLAYER2_ID):
                    return (None, 100000000000000)
                elif winning_move(board, PLAYER1_ID):
                    return (None, -10000000000000)
                else:  # Game is over, no more valid moves
                    return (None, 0)
            else:  # Depth is zero
                return (None, self.score_position(board, PLAYER2_ID))
        if maximizingPlayer:
            value = -math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = get_next_open_row(board, col)
                b_copy = board.copy()
                drop_piece(b_copy, col, PLAYER2_ID)
                new_score = self.minimax(b_copy, depth - 1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return column, value

        else:  # Minimizing player
            value = math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = get_next_open_row(board, col)
                b_copy = board.copy()
                drop_piece(b_copy, col, PLAYER1_ID)
                new_score = self.minimax(b_copy, depth - 1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value

    def evaluate_window(self, window, piece):
        score = 0
        opp_piece = PLAYER1_ID
        if piece == PLAYER1_ID:
            opp_piece = PLAYER2_ID

        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(EMPTY) == 1:
            score += 5
        elif window.count(piece) == 2 and window.count(EMPTY) == 2:
            score += 2

        if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
            score -= 4

        return score

    def score_position(self, board, piece):
        score = 0

        ## Score center column
        center_array = [int(i) for i in list(board[:, COLUMN_COUNT // 2])]
        center_count = center_array.count(piece)
        score += center_count * 3

        ## Score Horizontal
        for r in range(ROW_COUNT):
            row_array = [int(i) for i in list(board[r, :])]
            for c in range(COLUMN_COUNT - 3):
                window = row_array[c:c + WINDOW_LENGTH]
                score += self.evaluate_window(window, piece)

        ## Score Vertical
        for c in range(COLUMN_COUNT):
            col_array = [int(i) for i in list(board[:, c])]
            for r in range(ROW_COUNT - 3):
                window = col_array[r:r + WINDOW_LENGTH]
                score += self.evaluate_window(window, piece)

        ## Score posiive sloped diagonal
        for r in range(ROW_COUNT - 3):
            for c in range(COLUMN_COUNT - 3):
                window = [board[r + i][c + i] for i in range(WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece)

        for r in range(ROW_COUNT - 3):
            for c in range(COLUMN_COUNT - 3):
                window = [board[r + 3 - i][c + i] for i in range(WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece)

        return score
