import sys
from time import sleep

import pygame
from bullet import Bullet
from alien import Alien
from random import randint

def check_events(ai_settings, screen, stats, sb, play_button, practice_button, ship, aliens, 
    target, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stats.write_score()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, sb, ship, aliens, target, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship,
                aliens, bullets, mouse_x, mouse_y)
            check_practice_button(ai_settings, screen, stats, sb, practice_button, ship,
                target, bullets, mouse_x, mouse_y)

def check_keydown_events(event, ai_settings, screen, stats, sb, ship, aliens, target, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    # Elif for less sticking motion
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif (event.key == pygame.K_SPACE):
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        stats.write_score()
        sys.exit()
    # Press P to play
    elif (event.key == pygame.K_p) and not stats.game_active:
        start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)

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

def check_practice_button(ai_settings, screen, stats, sb, practice_button, ship, 
    target, bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks Play"""
    button_clicked = practice_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_practice(ai_settings, screen, stats, sb, ship, target, bullets)

def start_game(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # Hide the mouse cursor
    ai_settings.initialize_dynamic_settings()
    pygame.mouse.set_visible(False)
    stats.reset_stats()
    stats.game_active = True

    # Reset the scoreboard images.
    sb.prep_score(stats)
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ships()

    # Empty the list of aliens and bullets
    aliens.empty()
    bullets.empty()

    # Create a new fleet and center the ship
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

def start_practice(ai_settings, screen, stats, sb, ship, target, bullets):
    # Hide the mouse cursor
    ai_settings.initialize_dynamic_settings()
    pygame.mouse.set_visible(False)
    stats.reset_stats()
    stats.practice_active = True

    # Reset the scoreboard images.
    sb.prep_score(stats)

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

def update_screen(ai_settings, screen, stats, sb, ship, aliens, target,
    bullets, play_button, practice_button):
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
        aliens.draw(screen)
    if stats.practice_active:
        target.draw_target()
    # Draw the score information
    sb.show_score()

    # Draw the play button if the game is active
    # Draw it last to appear above all other elements
    if not stats.game_active and not stats.practice_active:
        play_button.draw_button()
        practice_button.draw_button()
    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Update position of bullets and get rid of old bullets."""    
    bullets.update()
    #screen_rect = screen.get_rect()
    
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)
    
    # Remove old bullets
    # Bad practice to alter list while looping through it, so loop a copy
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
        #if bullet.rect.right >= screen_rect.right:
            bullets.remove(bullet)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, 
        aliens, bullets):
    """Respond to bullet-alien collisions"""
    # Check for collisions
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)
    
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score(stats)
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # If fleet destroyed, start a new level
        # Destroy existing bullets and create a new fleet
        bullets.empty()
        ai_settings.increase_speed_invasion()
        create_fleet(ai_settings, screen, ship, aliens)

        # Increase level
        stats.level += 1
        sb.prep_level()

def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of alieans."""
    # Create an alien and find the number of aliens in a row
    # Spacing between each alien is euqal to one alien width
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, 
                    ship.rect.height, alien.rect.height)
    
    alien_width = alien.rect.width
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, alien_width, row_number)

def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    return int(available_space_x / (2 * alien_width))

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height - 
                            (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, alien_width, row_number):
    # Create alien and place it in a row
    alien = Alien(ai_settings, screen)
    alien.x = alien_width + 2 * alien_width * alien_number
    # x stores where the alien should be, alien rect object will move it on the screen 
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens reached an edge"""
    # Loop over all aliens in a group of sprites
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change fleet direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Update the positions of all aliens in the fleet"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)

    check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)

def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Respond to ship being hit by alien."""
    
    if stats.ships_left > 0:
        # Decrement ships_left
        stats.ships_left -= 1

        # Update scoreboard
        sb.prep_ships()

        # Empty list of of aliens and bullets
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Check if any aliens reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat the same as ship getting hit
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
            break

def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()