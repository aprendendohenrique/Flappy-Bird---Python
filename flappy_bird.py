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
        self.screen_rect = self.screen.get_rect()

        self.game_over = False

        self.bird = Bird(self)

        self.pipes = pygame.sprite.Group()
        self.pipe_x_pos = self.screen_rect.right
        self.tileset = int(self.settings.screen_height / 32)

        self.create_pipes()

    def run_game(self):
        while True:
            self.check_events()
            if not self.game_over:
                self.update_pipes()
                self.bird.update()
            self.update_screen()
            self.clock.tick(self.settings.fps)

    def update_screen(self):
        self.screen.fill(self.settings.screen_color)
        self.bird.blitme()
        self.pipes.draw(self.screen)
        pygame.display.flip()

    def player_hit(self):
        """Player hits the screen edge or any pipe"""
        self.bird.position_bird()
        self.create_pipes()


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
        self.pipes.empty()
        self.pipe_x_pos = self.screen_rect.right
        for _ in range(self.settings.pipe_goal):
            self.create_pipe()

    def create_pipe(self):
        random_pos = randint(1 + self.settings.opening_size, self.tileset - 2)
        for count in range(random_pos - self.settings.opening_size):
            if count < random_pos - self.settings.opening_size - 1:
                new_pipe = Pipe(self)
            else:
                new_pipe = Pipe(self, True)
                new_pipe.image = pygame.transform.flip(new_pipe.image, False, True)
            new_pipe.rect.y = 32 * count
            new_pipe.rect.right = self.pipe_x_pos
            self.pipes.add(new_pipe)
        for count in range(self.tileset, random_pos, -1):
            if count > random_pos + 1:
                new_pipe = Pipe(self)
            else:
                new_pipe = Pipe(self, True)
            new_pipe.rect.y = 32 * count
            new_pipe.rect.right = self.pipe_x_pos
            self.pipes.add(new_pipe)
        self.pipe_x_pos += 32 * self.settings.objects_size_scale * self.settings.pipe_x_distance

    def update_pipes(self):
        self.pipes.update()
        for pipe in self.pipes:
            if pipe.rect.right <= 0:
                pipe.kill()
                self.create_pipe()
        if pygame.sprite.spritecollideany(self.bird, self.pipes):
            self.player_hit()


fb = FlappyBird()
fb.run_game()