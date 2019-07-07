import pygame.font

class Target():

    def __init__(self, ai_settings, screen, msg):
        """Initialize button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.ai_settings = ai_settings

        # Set the dimensions and properties of the button
        self. width, self. height = 200, 50
        self.button_color = (255, 0, 0)
        self.text_color = (255, 255, 255)
        # None param means default font, 48 for size
        self.font = pygame.font.SysFont(None, 48)  

        # Build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top + self.height
        self.x = float(self.rect.x)

        # Button message needs to be prepped only once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button"""
        # If we don't pass a color, color will be transparent
        self.msg_image = self.font.render(msg, True, self.text_color,
            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_target(self):
        """Draw blank button and then draw message"""
        # Draw rectangle
        self.screen.fill(self.button_color, self.rect)
        # Add text
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def update(self):
        self.x += (self.ai_settings.target_direction * 
                    self.ai_settings.target_speed_factor)
        self.rect.x = self.x
        self.msg_image_rect.center = self.rect.center

    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True

    def center_target(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx