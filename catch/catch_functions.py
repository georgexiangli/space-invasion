import sys
import pygame
from person import Person
from ball import Ball
from random import randint

def check_events(ai_settings, screen, person):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, person)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, person)

def check_keydown_events(event, ai_settings, screen, person):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        person.moving_right = True
    # Elif for less sticking motion
    elif event.key == pygame.K_LEFT:
        person.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, person):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        person.moving_right = False
    elif event.key == pygame.K_LEFT:
        person.moving_left = False

def create_balls(ai_settings, screen, person, balls):
    """Create a set of balls"""
    create_ball(ai_settings, screen, balls)

def create_ball(ai_settings, screen, balls):
    # Create alien and place it in a row
    new_ball = Ball(ai_settings, screen)
    new_ball.x = randint(0, ai_settings.screen_width - new_ball.rect.width)
    # x stores where the alien should be, alien rect object will move it on the screen 
    new_ball.rect.x = new_ball.x
    balls.add(new_ball)

def update_screen(ai_settings, screen, person, balls):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    # Draw person
    person.blitme()
    # Draw balls, draw is a pygame function for your group
    balls.draw(screen)
    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_balls(ai_settings, screen, person, balls):
    if pygame.sprite.spritecollideany(person, balls):
        pygame.sprite.spritecollide(person, balls, True)
        create_ball(ai_settings, screen, balls)
    for ball in balls.sprites():
        ball.rect.y += ai_settings.balls_drop_speed
    check_balls_bottom(ai_settings, screen, balls)

def check_balls_bottom(ai_settings, screen, balls):
    """Check if any aliens reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for ball in balls.copy():
        if ball.rect.bottom >= screen_rect.bottom:
            # Treat the same as ship getting hit
            create_ball(ai_settings, screen, balls)
            balls.remove(ball)

