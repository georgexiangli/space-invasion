import sys
import pygame
from bullet import Bullet
from alien import Alien
from random import randint

def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    # Elif for less sticking motion
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif (event.key == pygame.K_SPACE):
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    if len(bullets) < ai_settings.bullets_allowed:
        # Create a new bullet and add to bullets group.
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # Draw ship
    ship.blitme()
    # Draw alien fleet, draw is a pygame function for your group
    aliens.draw(screen)
    
    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_bullets(bullets, screen):
    """Update position of bullets and get rid of old bullets."""    
    bullets.update()
    #screen_rect = screen.get_rect()

    # Remove old bullets
    # Bad practice to alter list while looping through it, so loop a copy
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
        #if bullet.rect.right >= screen_rect.right:
            bullets.remove(bullet)
    print(len(bullets))

def create_fleet(ai_settings, screen, aliens, ship):
    """Create a full fleet of alieans."""
    # Create an alien and find the number of aliens in a row
    # Spacing between each alien is euqal to one alien width
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, 
                    ship.rect.height, alien.rect.height)
    
    alien_width = alien.rect.width
    row_spacing = []
    for row_number in range(number_rows):
        row_spacing.append(randint(.5 * alien_width, 1.5 * alien_width))
        random_alien_spacing = []
        for alien_number in range(number_aliens_x):
            random_alien_spacing.append(randint(alien_width / 2, alien_width))
            create_alien(ai_settings, screen, aliens, alien_number, 
                            alien_width, row_number, row_spacing, random_alien_spacing)

def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    return int(available_space_x / (2 * alien_width))

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height - 
                            (3 * alien_height) - ship_height)
    #number_rows = int(available_space_y / (2 * alien_height))
    number_rows = int(available_space_y / (2.5 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, alien_width, 
                    row_number, row_spacing, random_alien_spacing):
    # Create alien and place it in a row
    alien = Alien(ai_settings, screen)
    #alien.x = alien_width + 2 * alien_width * alien_number
    alien.x = alien_width + alien_width * alien_number + sum(random_alien_spacing)
    # x stores where the alien should be, alien rect object will move it on the screen 
    alien.rect.x = alien.x
    #alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.y = (alien.rect.height + alien.rect.height * row_number 
                    + sum(row_spacing))
    aliens.add(alien)