from pygame.sprite import Sprite
import pygame


class Pipe(Sprite):
    """A class that manages all the pipes in the game."""

    def __init__(self, fb_game, top_pipe = False):
        super().__init__()
        self.settings = fb_game.settings
        self.screen = fb_game.screen
        self.screen_rect = self.screen.get_rect()

        if top_pipe:
            self.image = pygame.image.load("images/pipe_top.bmp")
        else:
            self.image = pygame.image.load("images/pipe.bmp")

        self.rect = self.image.get_rect()

        self.rect.right = self.screen_rect.right

        self.y = float(self.rect.y)
