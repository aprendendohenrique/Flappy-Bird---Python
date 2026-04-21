import sys

import pygame
from random import randint

from settings import Settings

from bird import Bird
from pipe import Pipe


class FlappyBird:
    """The main class that controls the game"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.settings.screen_size)

        self.bird = Bird(self)
        self.pipes = pygame.sprite.Group()
        self.create_pipes()

    def run_game(self):
        while True:
            self.check_events()
            self.update_screen()
            self.clock.tick(self.settings.fps)

    def update_screen(self):
        self.screen.fill(self.settings.screen_color)
        self.bird.update()
        self.pipes.draw(self.screen)
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

    def create_pipes(self):
        tileset = int(self.settings.screen_height / 32)
        random_pos = randint(1 + self.settings.opening_size, tileset-2)
        for count in range(random_pos - self.settings.opening_size):
            if count < random_pos-self.settings.opening_size-1:
                print(count, random_pos)
                new_pipe = Pipe(self)
            else:
                new_pipe = Pipe(self, True)
                new_pipe.image = pygame.transform.flip(new_pipe.image, False, True)
            new_pipe.rect.y = 32 * count
            self.pipes.add(new_pipe)
        for count in range(tileset, random_pos, -1):
            if count > random_pos+1:
                new_pipe = Pipe(self)
            else:
                new_pipe = Pipe(self, True)
            new_pipe.rect.y = 32 * count
            self.pipes.add(new_pipe)

fb = FlappyBird()
fb.run_game()