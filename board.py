import numpy as np

from core import ROW_COUNT, COLUMN_COUNT, PLAYER1_ID, PLAYER2_ID, WIN_BITMASK


# TODO: Convert to class

def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, col, piece_id):
    update_cell(board, col, get_next_open_row(board, col), piece_id)


def update_cell(board, col, row, piece_id):
    board[row][col] = piece_id


def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if (board[r][col] == 0):
            return r
    raise Exception(f"Column {col} is full. Please use is_valid_location() first")


def winning_move(board, piece_id):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            four_coords = [(c, r), (c + 1, r), (c + 2, r), (c + 3, r)]
            if all_match(board, four_coords, piece_id):
                return four_coords

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            four_coords = [(c, r), (c, r + 1), (c, r + 2), (c, r + 3)]
            if all_match(board, four_coords, piece_id):
                return four_coords

    # Check positively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            four_coords = [(c, r), (c + 1, r + 1), (c + 2, r + 2), (c + 3, r + 3)]
            if all_match(board, four_coords, piece_id):
                return four_coords

    # Check negatively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            four_coords = [(c, r), (c + 1, r - 1), (c + 2, r - 2), (c + 3, r - 3)]
            if all_match(board, four_coords, piece_id):
                return four_coords

    return []


def all_match(board, four_coords, piece_id):
    vals = []
    for (col, row) in four_coords:
        vals.append(board[row, col])
    return np.array_equal(vals, np.full(4, piece_id))


def update_with_win(board, piece_id, winning_coords):
    for (col, row) in winning_coords:
        update_cell(board, col, row, piece_id & WIN_BITMASK)


def is_terminal_node(board):
    return winning_move(board, PLAYER1_ID) \
           or winning_move(board, PLAYER2_ID) \
           or len(get_valid_locations(board)) == 0


def get_valid_locations(board):
    valid_locations = []
    for col in range(COLUMN_COUNT):
        if is_valid_location(board, col):
            valid_locations.append(col)
    return valid_locations


def moves_played(board):
    return np.count_nonzero(board)


def print_board(board):
    print(np.flip(board, 0))
