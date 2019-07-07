import pygame.font

class Button():

    def __init__(self, ai_settings, screen, msg):
        """Initialize button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button
        self. width, self. height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        # None param means default font, 48 for size
        self.font = pygame.font.SysFont(None, 48)  

        # Build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Button message needs to be prepped only once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button"""
        # If we don't pass a color, color will be transparent
        self.msg_image = self.font.render(msg, True, self.text_color,
            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw message"""
        # Draw rectangle
        self.screen.fill(self.button_color, self.rect)
        # Add text
        self.screen.blit(self.msg_image, self.msg_image_rect)

        

             