import numpy as np


def evaluate(sudoku_board):
    """
    Evaluates the Sudoku board and counts the number of mistakes.
    """
    score = 0
    # Check how many mistakes in a row
    for i in range(sudoku_board.board_size):
        row = sudoku_board.board[i]
        unique_row = np.unique(row)
        score += sudoku_board.board_size - len(unique_row)

    # Check how many mistakes in a col
    for j in range(sudoku_board.board_size):
        col = sudoku_board.board[:, j]
        unique_col = np.unique(col)
        score += sudoku_board.board_size - len(unique_col)

    # Check how many mistakes in a box
    for box_i in range(sudoku_board.box_size):
        for box_j in range(sudoku_board.box_size):
            box = sudoku_board.board[box_i * sudoku_board.box_size: (box_i + 1) * sudoku_board.box_size,
                                     box_j * sudoku_board.box_size: (box_j + 1) * sudoku_board.box_size]
            box_1d = box.flatten()
            score += sudoku_board.board_size - len(np.unique(box_1d))

    return score
