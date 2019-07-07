import pygame
from pygame.sprite import Sprite
from random import randint

class Ball(Sprite):
    """A class to represent balls in a game of catch."""
    def __init__(self, ai_settings, screen):
        """Initialize the ball and set its starting position."""
        super(Ball, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings


        # Load alien image and set its rect attribute
        self.image = pygame.image.load('/home/gli/CS/python/alien_invasion/images/alien.bmp')
        self.rect = self.image.get_rect()    

        # Draw balls at a random location at the top of the screen
        self.rect.x = self.rect.width #randint(0, self.screen.rect.width)
        self.rect.y = self.rect.height

    def blitme(self):
        """Draw the ball at its current location"""
        # Use the game screen and put the image and its associated rectangle
        self.screen.blit(self.image, self.rect)    