import os, sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame, sys
from game import Game
from text_rendering import Rendering
from colors import Colors

# game settings
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 620
NUM_ROWS = 20
NUM_COLS = 10
CELL_SIZE = 30

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tetris Game")

clock = pygame.time.Clock()

game = Game(NUM_ROWS, NUM_COLS, CELL_SIZE)
rendering = Rendering(screen, game)

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 250)

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == GAME_UPDATE and not game.game_over:
            game.move_down()
        
        if event.type == pygame.KEYDOWN:
            if game.game_over:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and not game.game_over:
                game.move_left()
            if event.key == pygame.K_RIGHT and not game.game_over:
                game.move_right()
            if event.key == pygame.K_DOWN and not game.game_over:
                game.move_down()
            if event.key == pygame.K_UP and not game.game_over:
                game.rotate()

    # drawing
    screen.fill(Colors.background_purple)           

    # score
    rendering.draw_score()
    
    # best score
    rendering.draw_best_score()

    # next figure
    rendering.draw_next_figure()

    # game over
    if game.game_over:
        rendering.draw_game_over()

    game.draw(screen)

    pygame.display.update()
    clock.tick(60) # FPS