import pygame
from colors import Colors

class Rendering:
    
    def __init__(self, screen, game):

        pygame.font.init()

        # text and font
        if pygame.font.match_font("georgia"):
            self.title_font = pygame.font.Font(pygame.font.match_font("georgia"), 27)
            self.score_pos_correction = 6
            self.best_score_pos_correction = 10
            self.height_pos_correction = 5
            self.game_over_pos_correction = 3

        else:
            self.title_font = pygame.font.Font(None, 40)
            self.score_pos_correction = 0
            self.best_score_pos_correction = 0
            self.height_pos_correction = 0
            self.game_over_pos_correction = 0

        self.screen = screen
        self.game = game


    def draw_score(self):
        '''
        Returns rendered text regarding the current score to the screen
        '''

        score_surface = self.title_font.render("Score", True, Colors.white)

        score_rect = pygame.Rect(320, 65, 170, 60) # на 35 пиксель больше чем у рамки

        self.screen.blit(score_surface, 
                         (365 + self.score_pos_correction, 
                          30 - self.height_pos_correction, 50, 50))
        
        pygame.draw.rect(self.screen, Colors.rec_purple, score_rect, 0, 10)

        score_value_surface = self.title_font.render(str(self.game.score), True, Colors.white) 
        score_value_rect = score_value_surface.get_rect(center = (score_rect.centerx, 
                                                                score_rect.centery))
        self.screen.blit(score_value_surface, score_value_rect)


    def draw_best_score(self):
        '''
        Returns rendered text regarding the best score to the screen
        '''

        best_score_surface = self.title_font.render("Best score", True, Colors.white)

        best_score_rect = pygame.Rect(320, 390, 170, 60)

        self.screen.blit(best_score_surface, 
                         (335 + self.best_score_pos_correction, 
                          355 - self.height_pos_correction, 50, 50))
        
        pygame.draw.rect(self.screen, Colors.rec_purple, best_score_rect, 0, 10)

        best_score_value_surface = self.title_font.render(str(self.game.best_score), True, Colors.white)
        best_score_value_rect = best_score_value_surface.get_rect(center = (best_score_rect.centerx, 
                                                                            best_score_rect.centery))
        self.screen.blit(best_score_value_surface, best_score_value_rect)


    def draw_next_figure(self):
        '''
        Returns rendered text regarding the next figure to the screen
        '''

        next_surface = self.title_font.render("Next", True, Colors.white)

        next_rect = pygame.Rect(320, 215, 170, 80) # начальная х, у, насколько продвинуься по х, у

        self.screen.blit(next_surface, (375, 180 - self.height_pos_correction, 50, 50))
        pygame.draw.rect(self.screen, Colors.rec_purple, next_rect, 0, 10)


    def draw_game_over(self):
        '''
        Returns rendered text regarding the game over to the screen
        '''

        game_over_surface = self.title_font.render("GAME OVER", True, Colors.white)

        self.screen.blit(game_over_surface, (320 + self.game_over_pos_correction, 520, 50, 50))
