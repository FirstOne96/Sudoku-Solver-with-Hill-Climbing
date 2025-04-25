from evaluation import evaluate


def hill_climbing(sudoku_board, strategies, max_iterations=1000, max_restarts=200):
    """
    Hill climbing algorithm to solve the Sudoku puzzle using different strategies.
    """
    results = {}

    for strategy in strategies:
        print(f"\n---> Using strategy: {strategy.__name__}")
        restarts_used = 0
        best_board = None
        best_score = float('inf')
        solution_found = False
        total_iterations = 0

        for restart in range(max_restarts):
            restarts_used += 1
            current_board = sudoku_board.init_random()
            current_score = evaluate(current_board)

            # Initialize plateau count to track stagnation
            plateau_count = 0

            print(f"Restart {restarts_used}: Initial score = {current_score}")

            if current_score == 0:
                print("✅ Solution found on initial board!")
                best_board = current_board
                best_score = 0
                solution_found = True
                break

            for iteration in range(max_iterations):
                total_iterations += 1

                new_board = strategy(current_board)
                new_score = evaluate(new_board)

                if new_score < current_score:
                    current_board = new_board
                    current_score = new_score

                    if new_score < best_score:
                        best_board = new_board
                        best_score = new_score

                    if new_score == 0:
                        print(f"✅ Solution found at restart {restarts_used}, iteration {iteration + 1}")
                        solution_found = True
                        break

                elif new_score == current_score:
                    plateau_count += 1
                    if plateau_count > 50:
                        print(f"Plateau detected at restart {restarts_used}, iteration {iteration + 1}")
                        break

            if solution_found:
                break

            print(f"> Restart {restarts_used} done, best score so far: {best_score}")

        results[strategy.__name__] = {
            'strategy': strategy.__name__,
            'solution_found': solution_found,
            'final_score': best_score,
            'restarts_used': restarts_used,
            'total_iterations': total_iterations,
            'best_board': best_board
        }

        print(f"\nSummary for {strategy.__name__}:")
        print(f"-> Solution found: {solution_found}")
        print(f"-> Final score: {best_score}")
        print(f"-> Restarts used: {restarts_used}/{max_restarts}")
        print("-" * 40)
        print(best_board)

    return results
