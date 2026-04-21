import sys

import pygame

from settings import Settings

from bird import Bird


class FlappyBird:
    """The main class that controls the game"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.settings.screen_size)

        self.bird = Bird(self)

    def run_game(self):
        while True:
            self.check_events()
            self.update_screen()
            self.clock.tick(self.settings.fps)

    def update_screen(self):
        self.screen.fill(self.settings.screen_color)
        self.bird.update()
        pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.keydown_event(event)

    def keydown_event(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_SPACE:
            self.bird.jump()

fb = FlappyBird()
fb.run_game()