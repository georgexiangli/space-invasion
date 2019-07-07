class Settings():
    """A class to store all settings for catch."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Person settings
        self.person_speed_factor = 1.5

        # Ball settings
        self.balls_drop_speed = 1