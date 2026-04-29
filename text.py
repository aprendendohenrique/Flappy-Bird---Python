import pygame.font
from pygame import font


class Text:
    """A class that create a manage texts"""

    def __init__(self, fb_game, msg, font_size, text_color, pos=(0, 0)):
        """Initialize text attributes."""
        self.screen = fb_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = fb_game.settings

        self.text_color = text_color
        self.pos = pos

        self.font = pygame.font.SysFont(None, font_size)

        self.prep_text(msg)

    def prep_text(self, msg):
        """Turn the text into a rendered image."""
        text_str = f"{msg}"
        self.text_image = self.font.render(text_str, True,
                                            self.text_color)

        # Display the text at the determined position
        self.text_rect = self.text_image.get_rect()
        self.text_rect.center = self.pos

    def show_text(self):
        self.screen.blit(self.text_image, self.text_rect)