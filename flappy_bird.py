import sys

import pygame
from random import randint
from random import choice
from time import sleep

import data
from text import Text
from button import Button
from settings import Settings
from bird import Bird
from pipe import Pipe


class FlappyBird:
    """The main class that controls the game"""

    def __init__(self):
        """Initialize all needed attributes."""
        pygame.init()
        pygame.mixer.init()

        self.settings = Settings()
        self.clock = pygame.time.Clock()

        # Screen
        self.screen = pygame.display.set_mode(self.settings.screen_size)
        self.screen_rect = self.screen.get_rect()

        # Game over boolean to controll the game
        self.game_over = True

        # Player's bird
        self.bird = Bird(self)

        # Play button
        self.button_msg = "Play"
        self.button = Button(self, self.button_msg)

        # Score/High Score texts
        score = data.load()
        print(score)
        if score:
            self.settings.high_score = score
        self.score_text = Text(self, msg=self.settings.score, font_size=48,
                               text_color=(0, 0, 0), pos=(self.screen_rect.right-30, 35))
        self.high_score_text = Text(self, msg=self.settings.high_score, font_size=48,
                                    text_color=(0, 0, 0), pos=(self.screen_rect.width/2, 35))

        # Pipes and the Tileset that the pipes goes in
        self.pipes = pygame.sprite.Group()
        self.pipe_x_pos = self.screen_rect.right
        self.tileset = int(self.settings.screen_height / 32)
        self.create_pipes()

        # Background music
        pygame.mixer.music.load("music_sounds/intro_theme.mp3")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

        # Sound effects
        self.jump_sound_1 = pygame.mixer.Sound("music_sounds/jump_1.wav")
        self.jump_sound_2 = pygame.mixer.Sound("music_sounds/jump_2.wav")
        self.jump_sound_3 = pygame.mixer.Sound("music_sounds/jump_3.wav")
        self.jump_sound_4 = pygame.mixer.Sound("music_sounds/jump_4.wav")
        self.jump_sound_5 = pygame.mixer.Sound("music_sounds/jump_5.wav")
        self.jump_sounds = [self.jump_sound_1, self.jump_sound_2, self.jump_sound_3,
                            self.jump_sound_4, self.jump_sound_5]
        self.hit_sound = pygame.mixer.Sound("music_sounds/hit.ogg")

    def run_game(self):
        """Where everything in the game is run every tick"""
        while True:
            self.check_events()
            if not self.game_over:
                self.update_pipes()
                self.bird.update()
            self.update_screen()
            self.clock.tick(self.settings.fps)

    def update_screen(self):
        """Update/Draw the elements of the game on the screen"""
        self.screen.fill(self.settings.screen_color)
        self.bird.blitme()
        self.pipes.draw(self.screen)
        if self.game_over:
            self.button.draw_button()
            self.high_score_text.show_text()
        else:
            self.score_text.show_text()
        pygame.display.flip()

    def player_hit(self):
        """Player hits the screen edge or any pipe"""
        self.game_over = True

        # Play the hit sound
        self.hit_sound.play()

        # A sleep time
        sleep(0.5)

        # Unpause the background music
        pygame.mixer.music.unpause()

        # Resets the score and update it.
        self.settings.score = 0
        self.score_text.prep_text(self.settings.score)
        self.high_score_text.prep_text(self.settings.high_score)

        # Reset the bird position and rotation.
        self.bird.rotate_bird(0)
        self.bird.position_bird()

        # Re-create all the pipes
        self.create_pipes()


    def check_events(self):
        """Checks for the keyboard/mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.keydown_event(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if self.button.rect.collidepoint(mouse_pos):
                    pygame.mixer.music.pause()
                    self.game_over = False

    def keydown_event(self, event):
        """Checks for all the keydown events."""
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_SPACE:
            self.bird.jump()
            choice(self.jump_sounds).play()
            if self.game_over:
                pygame.mixer.music.pause()
                self.game_over = False

    def create_pipes(self):
        """Creates the horizontal line of pipes"""
        # Empties the pipes first every time its called.
        self.pipes.empty()
        self.pipe_x_pos = self.screen_rect.right
        for _ in range(self.settings.pipe_goal):
            self.create_pipe()

    def create_pipe(self):
        """Create every single pipe in a vertical line."""
        # Sets a random position inside the tileset, to where the pipes will "meet". with screen boundaries.
        random_pos = randint(1 + self.settings.opening_size, self.tileset - 2)

        # Create the upper pipes
        for count in range(random_pos - self.settings.opening_size):
            # Checks if it still haven't reached the random position.
            if count < random_pos - self.settings.opening_size - 1:
                new_pipe = Pipe(self)
            else:
                # Creates a single pipe and position it.
                new_pipe = Pipe(self, True)
                new_pipe.image = pygame.transform.flip(new_pipe.image, False, True)
            new_pipe.rect.y = 32 * count
            new_pipe.rect.right = self.pipe_x_pos
            self.pipes.add(new_pipe)

        # Create the bottom pipes
        for count in range(self.tileset, random_pos, -1):
            # Checks if it still haven't reached the random position.
            if count > random_pos + 1:
                new_pipe = Pipe(self)
            else:
                # Creates a single pipe and position it.
                new_pipe = Pipe(self, True)
            new_pipe.rect.y = 32 * count
            new_pipe.rect.right = self.pipe_x_pos
            self.pipes.add(new_pipe)
        self.pipe_x_pos += 32 * self.settings.objects_size_scale * self.settings.pipe_x_distance

    def update_pipes(self):
        """Updates pipes position and check any collisions, or if it's outside the screen."""
        self.pipes.update()

        # A boolean so that the score is just added one time per loop.
        sc_check = False
        for pipe in self.pipes:
            # Check if the pipe is outside the screen.
            if pipe.rect.right <= 0:
                pipe.kill()
                self.create_pipe()

                # An if statement so that it's content is read only once in the loop.
                if not sc_check:
                    # Adds the score with score points and updates it.
                    self.settings.score += 1
                    self.score_text.prep_text(self.settings.score)
                    sc_check = True

                    # Check if the score is higher than the high_score and updates and saves it.
                    if self.settings.score > self.settings.high_score:
                        self.settings.high_score = self.settings.score
                        data.save(self.settings.high_score)

        # Check any collisions between the player and any pipe.
        if pygame.sprite.spritecollideany(self.bird, self.pipes):
            self.player_hit()

# Crate an instance of the game and runs it.
fb = FlappyBird()
fb.run_game()