import random
import pygame
from pygame.sprite import Sprite

# All values are % of the screen
# the gap between the top and the bottom pipe
vgap = 0.15

# the gap between the sets of pipes
hgap = 0.25

# the width of the pipes
width = 0.1

# minimum height of the pipes
minheight = 0.1

colour = pygame.Color(225, 255, 225)
class Obstacle:
    top = Sprite()
    bottom = Sprite()

    def __init__(self, surf: pygame.Surface, x: int):
        from main import (getWidth, getHeight)
        #generate distance
        topdist = random.random()
        buffer = minheight + hgap
        max = 1 - buffer
        if topdist > max:
            topdist = max
        bottomdist = 1 - topdist - hgap

        #top
        
        self.top.surf = pygame.Surface((getWidth(width), getHeight(topdist)))
        self.top.surf.fill(colour)
        self.top.rect = self.top.surf.get_rect()
        self.top.rect.topleft = (x, 0)

        #draw bottom
        self.bottom.surf = pygame.Surface((getWidth(width), getHeight(bottomdist)))
        self.bottom.surf.fill(colour)
        self.bottom.rect = self.bottom.surf.get_rect()
        self.bottom.rect.topleft = (x, getHeight(1-bottomdist))

        #draw on screen
        surf.blit(self.top.surf, self.top.rect)
        surf.blit(self.bottom.surf, self.bottom.rect)
        pygame.display.flip()
    
    def move(self, dist: int):
        """Move left a certain distance"""
        self.top.rect.move_ip(-dist, 0)
        self.bottom.rect.move_ip(-dist, 0)
        pygame.display.flip()
