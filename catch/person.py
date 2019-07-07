import pygame

class Person():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('/home/gli/CS/python/alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Location stored as a float to allow decimal speeds
        self.center = float(self.rect.centerx) 

        # Movement
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the person's position based on the movement flag"""
        # Two separate if blocks to allow holding down of left and right
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.person_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.person_speed_factor

        # Only integer part of self.center is stored in self.rect.centerx
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the person at its current location."""
        self.screen.blit(self.image, self.rect)
       