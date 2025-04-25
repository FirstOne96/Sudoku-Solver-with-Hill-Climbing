import numpy as np
import random


class SudokuBoard:
    def __init__(self, box_size):
        """
        Initializes a Sudoku board with the given box size.
        """
        self.box_size = box_size
        self.board_size = np.pow(box_size, 2)
        self.board = np.zeros((self.board_size, self.board_size), dtype=int)
        self.fixed_cells = np.zeros((self.board_size, self.board_size), dtype=bool)

    def read_board(self, filename):
        """
        Reads a Sudoku board from a file and initializes the board and fixed_cells attributes.
        """
        with open(filename, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                values = line.split()
                for j, value in enumerate(values):
                    if value == '0':
                        self.board[i][j] = 0
                        self.fixed_cells[i][j] = False
                    else:
                        self.board[i][j] = value
                        self.fixed_cells[i][j] = True
        return self

    def init_random(self):
        """
        Initializes the board with random values, ensuring that fixed cells remain unchanged.
        """
        for i in range(self.board_size):
            # Get the fixed positions and their values
            fixed_positions = np.where(self.fixed_cells[i, :])[0]
            fixed_values = set([self.board[i, j] for j in fixed_positions])

            # Generate a list of available values
            available_values = set(range(1, self.board_size + 1)) - fixed_values
            available_values = list(available_values)
            random.shuffle(available_values)

            # Fill the row with random values
            for j in range(self.board_size):
                if not self.fixed_cells[i][j]:
                    if len(available_values) > 0:
                        self.board[i][j] = available_values.pop()
                    else:
                        self.board[i][j] = 0
        return self

    def __deepcopy__(self, memo):
        """
        Create a deep copy
        """
        new_board = SudokuBoard(self.box_size)
        new_board.board = np.copy(self.board)
        new_board.fixed_cells = np.copy(self.fixed_cells)
        return new_board

    def __str__(self):
        """
        Returns a string representation of the board.
        """
        board_str = ""
        for i in range(self.board_size):
            if i > 0 and i % self.box_size == 0:
                board_str += "-" * (self.board_size * 2 + self.box_size - 1) + "\n"

            for j in range(self.board_size):
                if j > 0 and j % self.box_size == 0:
                    board_str += "| "
                board_str += str(self.board[i, j]) + " "
            board_str += "\n"
        return board_str


