import sys
import pygame
from raindrop import Raindrop

def check_events(ai_settings, screen):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, storm):
    """Update images on the screen and flip to the new screen."""
    screen.fill(ai_settings.bg_color)
    # Draw storm
    storm.draw(screen)
    # Show images
    pygame.display.flip()

def create_storm(ai_settings, screen, storm):
    """Create a full fleet of alieans."""
    # Create an alien and find the number of aliens in a row
    # Spacing between each alien is euqal to one alien width
    raindrop = Raindrop(ai_settings, screen)
    raindrop_width = raindrop.rect.width
    number_raindrops_x = get_number_raindrops_x(ai_settings, raindrop_width)
    number_rows = get_number_rows(ai_settings, raindrop.rect.height)
    
    for row_number in range(number_rows):
        for raindrop_number in range(number_raindrops_x):
            create_raindrop(ai_settings, screen, storm, raindrop_number, raindrop_width, row_number)

def get_number_raindrops_x(ai_settings, raindrop_width):
    available_space_x = ai_settings.screen_width - (2 * raindrop_width)
    return int(available_space_x / (2 * raindrop_width))

def get_number_rows(ai_settings, raindrop_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height - (3 * raindrop_height))
    number_rows = int(available_space_y / (2 * raindrop_height))
    return number_rows

def create_raindrop(ai_settings, screen, storm, raindrop_number, raindrop_width, row_number):
    # Create alien and place it in a row
    raindrop = Raindrop(ai_settings, screen)
    raindrop.x = raindrop_width + 2 * raindrop_width * raindrop_number
    # x stores where the raindrop should be, raindrop rect object will move it on the screen 
    raindrop.rect.x = raindrop.x
    # Need to update raindrop y, alien does not have a y attribute
    raindrop.y = raindrop.rect.height + 2 * raindrop.rect.height * row_number
    raindrop.rect.y = raindrop.y
    storm.add(raindrop)

def check_storm_edges(ai_settings, screen, storm):
    """Respond appropriately if any aliens reached an edge"""
    # Loop over all aliens in a group of sprites
    for raindrop in storm.sprites():
        if raindrop.check_edges():
            raindrop_number = get_number_raindrops_x(ai_settings, raindrop.rect.width)
            add_storm_row(ai_settings, screen, storm, raindrop_number, raindrop.rect.width, 0)
            break
    remove_old_rain(storm)

def remove_old_rain(storm):
    for raindrop in storm.sprites():
        if raindrop.check_edges():
            storm.remove(raindrop)

def add_storm_row(ai_settings, screen, storm, number_raindrops_x, raindrop_width, row_number):
    for raindrop_number in range(number_raindrops_x):
        create_raindrop(ai_settings, screen, storm, raindrop_number, raindrop_width, row_number)

def update_storm(ai_settings, screen, storm):
    """Update the positions of all raindrops in the storm"""
    check_storm_edges(ai_settings, screen, storm)
    storm.update()
