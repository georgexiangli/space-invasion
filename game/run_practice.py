import pygame
from t_settings import Settings
from t_ship import Ship
import practice_game_functions as pgf
from pygame.sprite import Group
from practice_stats import GameStats
from t_scoreboard import Scoreboard
from t_button import Button
from t_target import Target

def run_game():
    # Initialize game and create a screen object.
    pygame.init()

    # Initialize all settings as an object
    ai_settings = Settings()

    screen = pygame.display.set_mode((
        ai_settings.screen_width, 
        ai_settings.screen_height))
    pygame.display.set_caption("Target Practice")
    
    play_button = Button(ai_settings, screen, "Play")

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # Create ship object
    ship = Ship(ai_settings, screen)
    # Group to store bullets
    bullets = Group()
    target = Target(ai_settings, screen, "Target")

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        # Time interval? If it doesn't collect an event, bullets still update
        # Always check events in case user wants to exit out
        pgf.check_events(ai_settings, screen, stats, sb, play_button, ship, 
            target, bullets)
        
        if stats.game_active:
            # Update ship's location based on events checked
            ship.update()
            pgf.update_bullets(ai_settings, screen, stats, sb, ship, target, bullets)
            pgf.update_target(ai_settings, stats, screen, sb, ship, target, bullets)
        # Renders play button if game is inactive
        pgf.update_screen(ai_settings, screen, stats, sb, ship, target, 
            bullets, play_button)

run_game()