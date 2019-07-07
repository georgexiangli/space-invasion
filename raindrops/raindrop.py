import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """A class to represent a single raindrop in a storm."""

    def __init__(self, ai_settings, screen):
        """Initialize raindrop and set its starting position."""
        super(Raindrop, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load raindrop image and set its rect attribute
        self.image = pygame.image.load('/home/gli/CS/python/alien_invasion/images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new raindrop near the top left of the screen
        # By default, alien starts exactly at top left, these values offset it by a little
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if raindrop is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.top >= screen_rect.bottom:
            return True

    def update(self):
        self.y += self.ai_settings.drop_speed
        self.rect.y = self.y

    def blitme(self):
        """Draw the raindrop at its current location"""
        # Use the game screen and put the image and its associated rectangle
        self.screen.blit(self.image, self.rect)
