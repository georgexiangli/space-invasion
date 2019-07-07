import pygame, sys
#from gamebase import *
#from pygame.locals import *
pygame.init()


#Variables
MainSprites = pygame.sprite.Group()


#Classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

player = Player()
MainSprites.add(player)
print(MainSprites)

MainSprites = pygame.sprite.Group()
