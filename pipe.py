from pygame.sprite import Sprite
import pygame


class Pipe(Sprite):
    """A class that manages all the pipes in the game."""

    def __init__(self, fb_game, top_pipe = False):
        """Initialize all the attributes for the pipes"""
        super().__init__()
        self.settings = fb_game.settings
        self.screen = fb_game.screen
        self.screen_rect = self.screen.get_rect()

        # Checks if it's a normal pipe or the pipe that goes on the end of it.
        # Get its image.
        if top_pipe:
            self.image = pygame.image.load("images/pipe_top.bmp")
        else:
            self.image = pygame.image.load("images/pipe.bmp")

        # Scale the image with the scaling of the game.
        self.image_width = self.image.get_width()
        self.image_height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (
            self.image_width * self.settings.objects_size_scale, self.image_height * self.settings.objects_size_scale))

        # Get its rect and position the pipe.
        self.rect = self.image.get_rect()
        self.rect.right = self.screen_rect.right

        # Gets the rect "y" position with "float"
        self.y = float(self.rect.y)

    def update(self):
        """Makes the pipe move and kills it, if it goes outbound."""
        self.rect.x -= self.settings.pipe_speed
        if self.rect.right < 0:
            self.kill()
