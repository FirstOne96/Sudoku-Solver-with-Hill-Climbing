# 🧩 Sudoku Solver with Hill Climbing

This project implements a Sudoku solver using the Hill Climbing algorithm. It compares different strategies for generating neighboring states to find the best solution.

## ✨ Features
- Solves Sudoku puzzles of various sizes (e.g., 9x9, 16x16).
- Implements multiple strategies for generating neighbors:
  - Swap cells in a row.
  - Swap cells in a box.
  - Change the value in a cell.
- Supports configurable maximum iterations and restarts.
- Provides a summary of results, including the best strategy based on final score and iterations.

## 📋 Requirements
- Python 3.8 or higher
- Required Python packages (install via `pip`):
  - `numpy`

## 🚀 Installation
1. Clone the repository:
   ```bash
   git clone git@gitlab.fit.cvut.cz:kozloan3/bi-zum-ls2025-kozloan3.git
   cd bi-zum-ls2025-kozloan3/semestral
   ```
2. Install the required packages:
   ```bash
    pip install -r requirements.txt
    ```
3. Run the Sudoku solver:
    ```bash
    python3 app.py filename box_size
    ```
   * filename : Path to the Sudoku puzzle file (e.g., sudoku3x3(10).txt).
   * box_size: Size of the Sudoku box (e.g., 3 for 9x9, 4 for 16x16).

   Example:
    ```bash
    python3 app.py sudoku3x3(10).txt 3
    ```

## 📂 File Structure
- `app.py`: Main application file that runs the Sudoku solver.
- `board.py`: Contains the SudokuBoard class for managing the Sudoku board.
- `hill_climbing.py`: Implements the Hill Climbing algorithm and strategies.
- `algorithms.py`: Defines the neighbor generation strategies.
- `sudoku/`: Directory containing sample Sudoku puzzle files.

## 📈 Results
The program outputs a summary of the results, including:  
* Whether a solution was found.
* Final score.
* Number of restarts and iterations used.
* Best strategy based on final score and iterations.