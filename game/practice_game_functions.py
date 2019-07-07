import sys
from time import sleep
import pygame
from t_bullet import Bullet
from random import randint

def check_events(ai_settings, screen, stats, sb, play_button, ship, target, 
    bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stats.write_score()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, sb, ship, target, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship,
                target, bullets, mouse_x, mouse_y)

def check_keydown_events(event, ai_settings, screen, stats, sb, ship, target, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    # Elif for less sticking motion
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif (event.key == pygame.K_SPACE):
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        #stats.write_score()
        sys.exit()
    # Press P to play
    elif (event.key == pygame.K_p) and not stats.game_active:
        start_game(ai_settings, screen, stats, sb, ship, target, bullets)

def check_keyup_events(event, ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, 
    aliens, bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks Play"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)

def start_game(ai_settings, screen, stats, sb, ship, target, bullets):
    # Hide the mouse cursor
    ai_settings.initialize_dynamic_settings()
    pygame.mouse.set_visible(False)
    stats.reset_stats()
    stats.game_active = True

    # Reset the scoreboard images.
    sb.prep_score()

    # Empty the list of bullets
    bullets.empty()

    target.center_target()
    ship.center_ship()

def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    if len(bullets) < ai_settings.bullets_allowed:
        # Create a new bullet and add to bullets group.
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_screen(ai_settings, screen, stats, sb, ship, target, 
    bullets, play_button):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # Draw ship
    ship.blitme()
    # Draw alien fleet, draw is a pygame function for your group
    if stats.game_active:
        target.draw_target()
    # Draw the score information
    sb.show_score()

    # Draw the play button if the game is active
    # Draw it last to appear above all other elements
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, ship, target, bullets):
    """Update position of bullets and get rid of old bullets."""    
    bullets.update()
    
    check_bullet_target_collisions(ai_settings, screen, stats, sb, ship, target, bullets)
    
    # Remove old bullets
    # Bad practice to alter list while looping through it, so loop a copy
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def check_bullet_target_collisions(ai_settings, screen, stats, sb, ship, 
        target, bullets):
    """Respond to bullet-alien collisions"""
    # Check for collisions
    collisions = pygame.sprite.spritecollide(target, bullets, True)
    
    if collisions:
        stats.score += ai_settings.target_points
        sb.prep_score(stats)
        ai_settings.increase_speed_practice()

def check_target_edges(ai_settings, target):
    """Respond appropriately if target reached an edge"""
    # Loop over all aliens in a group of sprites
    if target.check_edges():
        change_target_direction(ai_settings, target)

def change_target_direction(ai_settings, target):
    """Drop the entire fleet and change fleet direction"""
    ai_settings.target_direction *= -1

def update_target(ai_settings, stats, screen, sb, ship, target, bullets):
    """Update the position of the target"""
    check_target_edges(ai_settings, target)
    target.update()
