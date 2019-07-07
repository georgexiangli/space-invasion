import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load alien image and set its rect attribute
        self.image = pygame.image.load('/home/gli/CS/python/alien_invasion/images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        # By default, alien starts exactly at top left, these values offset it by a little
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's position as a decimal
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True

    def update(self):
        self.x += (self.ai_settings.fleet_direction * 
                    self.ai_settings.alien_speed_factor)
        self.rect.x = self.x

    def blitme(self):
        """Draw the alien at its current location"""
        # Use the game screen and put the image and its associated rectangle
        self.screen.blit(self.image, self.rect)