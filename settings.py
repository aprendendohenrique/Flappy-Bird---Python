class Settings:
    """This class stores the main configuration of the game"""

    def __init__(self):
        # System Settings
        self.fps = 60

        # Screen Settings
        self.objects_size_scale = 2
        self.screen_width = (32 * self.objects_size_scale) * 5
        self.screen_height = (32 * self.objects_size_scale) *7
        self.screen_size = (self.screen_width, self.screen_height)
        self.screen_color = (200, 200, 200)

        # Player Bird's Settings
        self.bird_x_offset = 1
        self.starter_falling_speed = 5
        self.jump_speed = 12
        self.jump_speed_decay = 1