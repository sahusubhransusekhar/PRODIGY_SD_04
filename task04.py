def print_grid(grid):
    """Helper function to print the Sudoku grid."""
    for row in grid:
        print(" ".join(str(num) for num in row))

def is_valid(grid, row, col, num):
    """Check if num can be placed at grid[row][col]."""
    # Check row
    if num in grid[row]:
        return False

    # Check column
    for r in range(9):
        if grid[r][col] == num:
            return False

    # Check 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if grid[r][c] == num:
                return False

    return True

def solve_sudoku(grid):
    """Solve the Sudoku puzzle using backtracking."""
    empty = find_empty_location(grid)
    if not empty:
        return True  # Puzzle solved

    row, col = empty

    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0  # Reset on backtrack

    return False

def find_empty_location(grid):
    """Find an empty location in the grid (represented by 0)."""
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None

def main():
    # Example Sudoku puzzle (0 represents empty cells)
    grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Original Sudoku puzzle:")
    print_grid(grid)

    if solve_sudoku(grid):
        print("\nSolved Sudoku puzzle:")
        print_grid(grid)
    else:
        print("No solution exists")

if __name__ == "__main__":
    main()