import pygame.image


class Bird:
    """The class that manages the player's bird"""

    def __init__(self, fp_game):
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

        # Position the bird in the midleft position of the screen
        self.rect.midleft = self.screen_rect.midleft
        self.rect.x += self.rect.width * self.settings.bird_x_offset

        # Store's the y position
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.falling_speed
        self.rect.y = self.y
        if self.jumping:
            if self.falling_speed < self.settings.starter_falling_speed:
                self.falling_speed += self.settings.jump_speed_decay
            else:
                self.falling_speed = self.settings.starter_falling_speed
                self.jumping = False
        self.blitme()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def jump(self):
        self.falling_speed = -self.settings.jump_speed
        self.jumping = True