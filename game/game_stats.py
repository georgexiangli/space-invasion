class GameStats():
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start Alien Invasion in an inactive state
        self.game_active = False
        self.practice_active = False
        # Don't reset for every game
        self.high_score = self.read_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def read_score(self):
        high_score = 0
        file = open('/home/gli/CS/python/alien_invasion/high_score.txt','r')
        read_score = file.readline()
        if read_score:
            high_score = int(read_score)
        file.close()
        return high_score

    def write_score(self):
        file = open('/home/gli/CS/python/alien_invasion/high_score.txt','w')
        file.write(str(self.high_score))
        file.close()