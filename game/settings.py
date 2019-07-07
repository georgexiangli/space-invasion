class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        #self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Bullet settings
        #self.bullet_speed_factor = 1
        self.bullet_width = 10
        self.bullet_height = 15
        # Tuple
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5

        # Alien settings
        #self.alien_speed_factor = 1
        self.fleet_drop_speed = 5
        # fleet_direction of 1 represents right, -1 represents left
        #self.fleet_direction = 1

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.target_speed_factor = 1
        self.ship_speed_factor = 1.5
        # Scoring
        self.alien_points = 50

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1 

        # Scoring
        self.target_points = 1

        # target_direction of 1 represents right; -1 represents left
        self.target_direction = 1 

    def increase_speed_invasion(self):
        """Increase speed settings and alien point values"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

    def increase_speed_practice(self):
        """Increase speed settings and alien point values"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.target_speed_factor *= self.speedup_scale