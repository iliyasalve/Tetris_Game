import pygame
from colors import Colors

class Grid:
    def __init__(self, num_rows: int, num_cols: int, cell_size: int):

        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size = cell_size

        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]

        self.colors = Colors.get_cell_colors()


    def is_inside(self, row: int, column: int) -> bool:
        '''
        Returns true if the passed coordinates are within the playing field, 
        otherwise returns false
        '''

        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        
        return False
    

    def is_empty(self, row: int, column: int) -> bool:
        '''
        Returns true if the cell at the selected coordinate is empty (that is, equal to 0), 
        otherwise returns false
        '''

        if self.grid[row][column] == 0:
            return True
        
        return False
    

    def is_row_full(self, row: int) -> bool:
        '''
        Returns true if all cells in a particular row are filled 
        (that is, each cell in the row is equal to 1), 
        otherwise returns false
        '''

        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
            
        return True
    
    
    def clear_row(self, row: int):
        '''
        Clears a row of filled cells
        '''

        for column in range(self.num_cols):
            self.grid[row][column] = 0


    def move_row_down(self, row: int, num_rows: int):
        '''
        Moves the top filled cells down
        '''

        for column in range(self.num_cols):
            self.grid[row + num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0


    def clear_full_rows(self):
        '''
        Returns the number of rows cleared at one time
        '''

        completed = 0

        for row in range(self.num_rows - 1, 0, -1):

            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1

            elif completed > 0:
                self.move_row_down(row, completed)

        return completed
    

    def reset(self):
        '''
        Resetting the playing field to its original position
        '''

        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]


    def draw(self, screen):
        '''
        Drawing a grid 
        '''

        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column * self.cell_size + 11, row * self.cell_size + 11, self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect) # касательно цвета, то мы берем цвет с индексом 0
