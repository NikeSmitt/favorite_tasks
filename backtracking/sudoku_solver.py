from pprint import *

# from console import *

"""
i - row, j - coloum, board - 2-dim array, count - position counter

Starting with an incomplete board:

1.Find some empty space
2.Attempt to place the digits 1-9 in that space
3.Check if that digit is valid in the current spot based on the current board
4.a. If the digit is valid, recursively attempt to fill the board using steps 1-3.
4.b. If it is not valid, reset the square you just filled and go back to the previous step.
5.Once the board is full by the definition of this algorithm we have found a solution.
"""

# board = [[0]*9 for i in range(9)]


board = [[0, 2, 9, 0, 0, 0, 4, 0, 0],
         [5, 0, 0, 4, 0, 6, 7, 0, 0],
         [0, 3, 0, 0, 7, 9, 0, 0, 8],
         [0, 0, 5, 0, 0, 0, 0, 8, 0],
         [0, 1, 0, 0, 4, 0, 3, 0, 2],
         [9, 0, 0, 1, 8, 3, 0, 0, 0],
         [4, 0, 8, 3, 0, 0, 9, 7, 0],
         [0, 0, 7, 6, 0, 0, 0, 5, 0],
         [1, 0, 0, 0, 9, 0, 2, 0, 0]]

board_solved = [[7, 2, 9, 8, 5, 1, 4, 3, 6],
           [5, 8, 1, 4, 3, 6, 7, 2, 9],
           [6, 3, 4, 2, 7, 8, 5, 7, 7],
           [3, 4, 5, 9, 6, 2, 1, 8, 7],
           [8, 1, 6, 5, 4, 7, 3, 9, 2],
           [9, 7, 2, 1, 8, 3, 6, 4, 5],
           [4, 6, 8, 3, 2, 5, 9, 7, 1],
           [2, 9, 7, 6, 1, 4, 8, 5, 3],
           [1, 5, 3, 7, 9, 8, 2, 6, 4]]


def isLegal(row, col, num, board):

    # check row
    for index in range(9):
        if num == board[row][index] and index != col:
            return False

    # check colomn
    for index in range(9):
        if num == board[index][col] and index != row:
            return False

    # check box 3X3, first - found initial pos for one from nine box
    # second - loop through cell in the box

    initialRow = 3 * (row // 3)
    initialColomn = 3 * (col // 3)

    for index in range(9):
        if num == board[initialRow + index // 3][initialColomn + index % 3]:
            if initialRow + index // 3 == row and initialColomn + index % 3 == col:
                continue
            return False

    return True


def sudokuSolver(count, board):
    # use count to iterate all cells in board
    if count == 81:
        pprint(board)
        return True

    # find free cell, which are not preset
    while board[count // 9][count % 9] != 0:
        count += 1
    else:
        for num in range(1, 10):

            if isLegal(count // 9, count % 9, num, board):
                board[count // 9][count % 9] = num
                if sudokuSolver(count + 1, board):
                    return True
                else:
                	board[count // 9][count % 9] = 0    
        # this is very important row!!!
        


def solveSudoku(board):
    count = 0
    return sudokuSolver(count, board)


print(solveSudoku(board))


