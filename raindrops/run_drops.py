import pygame
from settings import Settings
from raindrop import Raindrop
import rain_functions as rf
from pygame.sprite import Group

def run_drops():
    # Initialize game and create screen object
    pygame.init()

    # Initialize settings object
    ai_settings = Settings()

    screen = pygame.display.set_mode((            
            ai_settings.screen_width, 
            ai_settings.screen_height))
    pygame.display.set_caption("Rain")

    storm = Group()
    rf.create_storm(ai_settings, screen, storm)

    while True:
        rf.check_events(ai_settings, screen)
        rf.update_storm(ai_settings, screen, storm)
        rf.update_screen(ai_settings, screen, storm)

run_drops()