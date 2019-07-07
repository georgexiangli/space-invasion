import pygame
from catch_settings import Settings
from ball import Ball
from person import Person
from pygame.sprite import Group
import catch_functions as cf

def run_catch():
    # Initialize game and create a screen object.
    pygame.init()

    # Initialize all settings as an object
    ai_settings = Settings()

    screen = pygame.display.set_mode((
        ai_settings.screen_width, 
        ai_settings.screen_height))
    pygame.display.set_caption("Catch")

    # Create person
    person = Person(ai_settings, screen)
    # Create ball
    balls = Group()
    cf.create_balls(ai_settings, screen, person, balls)

    # Start the main loop for the game
    while True:
        # Watch for keyboard and mouse movements
        cf.check_events(ai_settings, screen, person)
        person.update()
        cf.update_balls(ai_settings, screen, person, balls)
        cf.update_screen(ai_settings, screen, person, balls)

run_catch()