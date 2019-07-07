import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
import practice_game_functions as pgf
from t_target import Target

def run_game():
    # Initialize game and create a screen object.
    pygame.init()

    # Initialize all settings as an object
    ai_settings = Settings()

    screen = pygame.display.set_mode((
        ai_settings.screen_width, 
        ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    play_button = Button(ai_settings, screen, "Play", False)
    practice_button = Button(ai_settings, screen, "Practice", True)

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # Create ship object
    ship = Ship(ai_settings, screen)
    # Group to store bullets
    bullets = Group()
    # Make an alien fleet
    aliens = Group()
    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    target = Target(ai_settings, screen, "Target")

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        # Time interval? If it doesn't collect an event, bullets still update
        # Always check events in case user wants to exit out
        gf.check_events(ai_settings, screen, stats, sb, play_button, practice_button, ship, 
            aliens, target, bullets)
        
        if stats.game_active:
            # Update ship's location based on events checked
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, 
                bullets)

        if stats.practice_active:
            # Update ship's location based on events checked
            ship.update()
            pgf.update_bullets(ai_settings, screen, stats, sb, ship, target, bullets)
            pgf.update_target(ai_settings, stats, screen, sb, ship, target, bullets)
        # Renders play button if game is inactive
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, target, 
            bullets, play_button, practice_button)

run_game()