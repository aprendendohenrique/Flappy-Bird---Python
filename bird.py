import pygame
from pygame.event import set_keyboard_grab


class Bird:
    """The class that manages the player's bird"""

    def __init__(self, fp_game):
        self.fp_game = fp_game
        self.settings = fp_game.settings
        self.screen = fp_game.screen
        self.screen_rect = self.screen.get_rect()
        self.falling_speed = self.settings.starter_falling_speed
        self.jumping = False

        # Get the bird image, scale it, and get its rect
        self.image = pygame.image.load("images/flappy_bird.bmp")
        self.image_width = self.image.get_width()
        self.image_height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (
            self.image_width * self.settings.objects_size_scale, self.image_height * self.settings.objects_size_scale))
        self.rect = self.image.get_rect()
        self.rotated_image = pygame.transform.rotate(self.image, 0)

        # Position the bird in the midleft position of the screen
        self.position_bird()

        # Store's the y position
        self.y = float(self.rect.y)

    def update(self):
        self.check_screen_edge()
        self.y += self.falling_speed
        self.rect.y = self.y
        if self.jumping:
            if self.falling_speed < self.settings.starter_falling_speed:
                self.falling_speed += self.settings.jump_speed_decay
            else:
                self.falling_speed = self.settings.starter_falling_speed
                self.jumping = False
                self.rotate_bird(-45)

    def blitme(self):
        self.screen.blit(self.rotated_image, self.rect)

    def jump(self):
        self.falling_speed = -self.settings.jump_speed
        self.rotate_bird(45)
        self.jumping = True

    def rotate_bird(self, angle):
        self.rotated_image = pygame.transform.rotate(self.image, angle)
        self.rect = self.rotated_image.get_rect(center=self.rect.center)

    def check_screen_edge(self):
        if self.rect.bottom >= self.screen_rect.bottom:
            self.fp_game.player_hit()
        elif self.rect.top <= 0:
            self.fp_game.player_hit()

    def position_bird(self):
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
        self.rect.x += self.rect.width * self.settings.bird_x_offset