class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Bullet settings
        self.bullet_width = 5
        self.bullet_height = 15
        # Tuple
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        self.speedup_scale = 1.05
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.bullet_speed_factor = 3
        self.target_speed_factor = 1
        self.ship_speed_factor = 1.5
        # Scoring
        self.target_points = 1

        # target_direction of 1 represents right; -1 represents left
        self.target_direction = 1 

    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.target_speed_factor *= self.speedup_scale