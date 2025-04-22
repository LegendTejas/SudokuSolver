#Sudoku Solver using Backtracking
class Solution:
    def solveSudoku(self, board):
        self.solve(board)

    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for c in map(str, range(1, 10)):  # Trying numbers '1' to '9'
                        if self.isValid(board, i, j, c):
                            board[i][j] = c
                            if self.solve(board):  # Recursively solve
                                return True
                            
                            board[i][j] = '.'  # Backtrack if no solution found
                    return False  # No valid number found, backtrack
        return True  # Sudoku solved

    def isValid(self, board, row, col, c):
        for i in range(9):
            if (board[i][col] == c or  # Check column
                board[row][i] == c or  # Check row
                board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c):  # Check 3x3 grid
                return False
        return True
    

board = [
    [".", ".", "9", "7", "4", "8", ".", ".", "."],
    ["7", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "2", ".", "1", ".", "9", ".", ".", "."],
    [".", ".", "7", ".", ".", ".", "2", "4", "."],
    [".", "6", "4", ".", "1", ".", "5", "9", "."],
    [".", "9", "8", ".", ".", ".", "3", ".", "."],
    [".", ".", ".", "8", ".", "3", ".", "2", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "6"],
    [".", ".", ".", "2", "7", "5", "9", ".", "."]
]


solver = Solution()
solver.solveSudoku(board)

for row in board:
    print(row)