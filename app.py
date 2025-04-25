from board import SudokuBoard
from algorithms import swap_cells_in_row, swap_cells_in_box, change_value_in_cell
from hill_climbing import hill_climbing
import sys


def main():
    """
    Main function to run the hill climbing algorithm on a Sudoku puzzle.
    """

    # Read filename and box size from stdin
    if len(sys.argv) >= 3:
        filename = sys.argv[1]
        box_size = int(sys.argv[2])
    else:
        print("Enter filename (e.g., sudoku4x4(30).txt):")
        filename = input().strip()
        print("Enter box size (e.g., 3 for 9x9, 4 for 16x16):")
        box_size = int(input().strip())

    board = SudokuBoard(box_size)
    board.read_board(f'sudoku/{filename}')

    results = hill_climbing(board, [swap_cells_in_row, swap_cells_in_box, change_value_in_cell],
                            max_iterations=1000, max_restarts=200)

    print("\n==== SUMMARY ====")
    for strategy_name, data in results.items():
        status = "✓" if data['solution_found'] else "✗"
        print(f"{status} {strategy_name}: score={data['final_score']}, "
              f"restarts={data['restarts_used']}, "
              f"iterations={data['total_iterations']}, ")

    # Find the best strategy based on different metrics
    best_by_score = min(results.items(), key=lambda x: x[1]['final_score'])
    best_by_iterations = min(results.items(), key=lambda x: x[1]['total_iterations'])

    print(f"\nBest strategy by final score: {best_by_score[0]}")
    print(f"Best strategy by iterations: {best_by_iterations[0]}")


if __name__ == "__main__":
    main()
