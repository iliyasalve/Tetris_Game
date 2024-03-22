import os

from grid import Grid
from figures import *
import random

class Game:
    def __init__(self, num_rows, num_cols, cell_size):

        self.grid = Grid(num_rows, num_cols, cell_size)

        self.cell_size = cell_size
        self.score = 0
        self.best_score = self.load_best_score()
        self.game_over = False

        self.initialization_blocks()
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        
        
    def update_score(self, lines_cleared, points):
        '''
        Game score update
        '''

        if lines_cleared == 1:
            self.score += 10
        if lines_cleared == 2:
            self.score += 30
        if lines_cleared >= 3:
            self.score += 50

        self.score += points

    
    def load_best_score(self):
        '''
        Loading a saved best game score from a file. 
        If there is no such file, then the default value is used
        '''

        if os.path.exists('data/highscore.data'):
            with open("data/highscore.data", "r") as f:
                best_score = int(f.read())
        else:
            best_score = 0

        return best_score
    

    def save_best_score(self):
        '''
        Saving the best game score to a file
        '''

        if self.score > self.best_score:
            self.best_score = self.score
            with open("data/highscore.data", "w") as f:
                f.write(str(self.best_score))


    def initialization_blocks(self):
        '''
        Initializing the figures
        '''

        self.blocks = [IBlock(self.cell_size), 
                       JBlock(self.cell_size), 
                       LBlock(self.cell_size), 
                       OBlock(self.cell_size), 
                       SBlock(self.cell_size),
                       ZBlock(self.cell_size),
                       TBlock(self.cell_size)]
        

    def get_random_block(self):
        '''
        Returns a random figure
        '''

        if len(self.blocks) == 0:
            self.initialization_blocks()
            
        block = random.choice(self.blocks)
        self.blocks.remove(block)

        return block
        

    def move_left(self):
        '''
        Moving a figure to the left
        '''

        self.current_block.move(0, -1)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(0, 1)


    def move_right(self):
        '''
        Moving a figure to the right
        '''

        self.current_block.move(0, 1)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(0, -1)


    def move_down(self):
        '''
        Moving a figure to the down
        '''

        self.current_block.move(1, 0)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(-1, 0)
            self.lock_block()


    def lock_block(self):
        '''
        Fixing a figure after touching the bottom level of the playing field 
        or the top of another figure
        '''

        tiles = self.current_block.get_cell_positions()

        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id

        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        self.update_score(rows_cleared, 0)

        if not self.block_fits():
            self.game_over = True


    def reset(self):
        '''
        Resetting the game process to its original state
        '''

        self.grid.reset()
        self.initialization_blocks()
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.save_best_score()
        self.score = 0


    def block_fits(self):
        '''
        Returns true if there are empty cells where the figure can move,
        otherwise returns false
        '''

        tiles = self.current_block.get_cell_positions()

        for tile in tiles:
            if not self.grid.is_empty(tile.row, tile.column):
                return False
            
        return True


    def rotate(self):
        '''
        Rotating a figure on the playing field
        '''

        self.current_block.rotate()

        if not self.block_inside() or not self.block_fits():
            self.current_block.over_rotation()


    def block_inside(self):
        '''
        Returns true if a figure is within the playing field, 
        otherwise returns false
        '''

        tiles = self.current_block.get_cell_positions()

        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.column):
                return False
        
        return True
    

    def draw(self, screen):
        '''
        Draws figures on the playing field
        '''

        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)
        
        match self.next_block.id:
            case 3:
                self.next_block.draw(screen, 255, 240)
            case 4:
                self.next_block.draw(screen, 255, 225)
            case _:
                self.next_block.draw(screen, 270, 225)
        