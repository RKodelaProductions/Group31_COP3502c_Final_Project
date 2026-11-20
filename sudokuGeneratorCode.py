import math, random

class SudokuGenerator:
    """
    create a sudoku board- initialize class variables and set up the 2D board
    This should initialize:
    self.row_length
    self.removed_cells
    self.board
    self.box_length

    Parameters:
    row_length is the number of rows/columns of the board
    removed_cells is an integer value -  the number of cells to be removed

    Return:
    None
    """
    def __init__(self, row_length, removed_cells):
        self.row_length= removed_cells
        self.removed_cells = removed_cells
        self.board = [[0 for _ in range(row_length)] for _ in range(row_length)]
        self.box_length = int(math.sqrt(row_length))

    '''
    Returns a 2D python list of numbers which represent the board
    Parameters: None
    Return: list[list]
    '''
    def get_board(self):
        return self.board

    '''
    Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes
    Parameters: NOne
    Return: None
    '''
    def print_board(self):
        for row in self.board:
            print(" ".join(str(num) for num in row) )
        print()