class Settings:
    """This class stores the main configuration of the game"""

    def __init__(self):
        """System Settings"""
        self.fps = 60

        """Screen Settings"""
        self.objects_size_scale = 2
        self.screen_width = (32 * self.objects_size_scale) * 5
        self.screen_height = (32 * self.objects_size_scale) * 7
        self.screen_size = (self.screen_width, self.screen_height)
        self.screen_color = (200, 200, 200)

        """Player Bird's Settings"""
        self.bird_x_offset = 1
        self.starter_falling_speed = 4
        self.jump_speed = 10
        self.jump_speed_decay = 1

        """Pipes settings"""
        # Integer Numbers
        self.opening_size = 4
        self.pipe_x_distance = 3.5
        self.pipe_goal = 15
        self.pipe_speed = 1.8