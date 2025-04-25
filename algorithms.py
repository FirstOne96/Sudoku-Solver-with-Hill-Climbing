import numpy as np
import random
from copy import deepcopy


def swap_cells_in_row(sudoku_board):
    """
    Swap 2 non-fixed cells in a random row
    """
    # Create a deepcopy
    new_board = deepcopy(sudoku_board)

    # Select a random row
    row = random.randrange(0, sudoku_board.board_size - 1)

    # Find non-fixed cells
    non_fixed = np.where(~sudoku_board.fixed_cells[row, :])[0]

    if len(non_fixed) >= 2:
        # We choose 2 cells to swap
        non_fixed_list = non_fixed.tolist()

        i, j = random.sample(non_fixed_list, 2)
        new_board.board[row, i], new_board.board[row, j] = new_board.board[row, j], new_board.board[row, i]

    return new_board


def swap_cells_in_box(sudoku_board):
    """
    Swap 2 random non-fixed cells in a random box
    """

    # Create a deepcopy
    new_board = deepcopy(sudoku_board)

    # Select a random box
    box_row = random.randrange(0, sudoku_board.box_size - 1)
    box_col = random.randrange(0, sudoku_board.box_size - 1)

    # Get box's coordinates
    row_start = box_row * sudoku_board.box_size
    row_end = (box_row + 1) * sudoku_board.box_size
    col_start = box_col * sudoku_board.box_size
    col_end = (box_col + 1) * sudoku_board.box_size

    # Find non-fixed cells in the chosen box
    non_fixed_cells = []
    for i in range(row_start, row_end):
        for j in range(col_start, col_end):
            if not sudoku_board.fixed_cells[i, j]:
                non_fixed_cells.append((i,j))

    if len(non_fixed_cells) >= 2:
        # Choose 2 cells to swap in the chosen box
        i, j = random.sample(non_fixed_cells, 2)
        new_board.board[i], new_board.board[j] = new_board.board[j], new_board.board[i]

    return new_board


def change_value_in_cell(sudoku_board):
    """
    Change a single non-fixed cell to a new random value
    """
    new_board = deepcopy(sudoku_board)
    non_fixed = np.where(~sudoku_board.fixed_cells)
    coords = list(zip(non_fixed[0], non_fixed[1]))

    if coords:
        i, j = random.choice(coords)

        curr = new_board.board[i, j]
        options = [x for x in range(1, sudoku_board.board_size + 1) if x != curr]
        new_value = random.choice(options)

        new_board.board[i, j] = new_value

    return new_board
