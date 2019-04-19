import numpy as np

from core import ROW_COUNT, COLUMN_COUNT, HUMAN_PIECE, AI_PIECE


def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def all_match(four_tiles, piece):
    return np.array_equal(four_tiles, np.full(4, piece))


def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            four_tiles = [board[r][c], board[r][c + 1], board[r][c + 2], board[r][c + 3]]
            if all_match(four_tiles, piece):
                return four_tiles

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            four_tiles = [board[r][c], board[r + 1][c], board[r + 2][c], board[r + 3][c]]
            if all_match(four_tiles, piece):
                return four_tiles

    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            four_tiles = [board[r][c], board[r + 1][c + 1], board[r + 2][c + 2], board[r + 3][c + 3]]
            if all_match(four_tiles, piece):
                return four_tiles

    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            four_tiles = [board[r][c], board[r - 1][c + 1], board[r - 2][c + 2], board[r - 3][c + 3]]
            if all_match(four_tiles, piece):
                return four_tiles

    return []


def is_terminal_node(board):
    return winning_move(board, HUMAN_PIECE) or winning_move(board, AI_PIECE) or len(get_valid_locations(board)) == 0


def get_valid_locations(board):
    valid_locations = []
    for col in range(COLUMN_COUNT):
        if is_valid_location(board, col):
            valid_locations.append(col)
    return valid_locations


def print_board(board):
    print(np.flip(board, 0))