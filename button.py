import pygame.font


class Button:
    """A class to build buttons for the game."""

    def __init__(self, fb_game, msg):
        """Initialize buttons attributes."""
        self.screen = fb_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = fb_game.settings

        # Set the dimensions and properties of the button.
        self.width, self.height = 75 * self.settings.objects_size_scale, 20 * self.settings.objects_size_scale
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 24 * self.settings.objects_size_scale)

        # Builds the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into rendered image and center the text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)