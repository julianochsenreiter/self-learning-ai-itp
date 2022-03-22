import random
import pygame
from pygame.sprite import Sprite
from pygame.surface import Surface

# All values are % of the screen
# the gap between the top and the bottom pipe
vgap = 0.15

# the gap between the sets of pipes
hgap = 0.25

# the width of the pipes
width = 0.1

# minimum height of the pipes
minheight = 0.1

OBSTC = pygame.Color(225, 255, 225)
class Obstacle:
    top = Sprite()
    bottom = Sprite()
    surf = None

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
        self.top.rect = self.top.surf.get_rect()
        self.top.rect.topleft = (x, 0)

        #bottom
        self.bottom.surf = pygame.Surface((getWidth(width), getHeight(bottomdist)))
        self.bottom.rect = self.bottom.surf.get_rect()
        self.bottom.rect.topleft = (x, getHeight(1-bottomdist))

        #save surface
        self.surf = surf

    def draw(self):
        """draw on screen"""
        pygame.draw.rect(self.surf, OBSTC, self.top.rect)
        pygame.draw.rect(self.surf, OBSTC, self.bottom.rect)
    
    def move(self, dist: int):
        """Move left a certain distance"""
        self.top.rect.move_ip(-dist, 0)
        self.bottom.rect.move_ip(-dist, 0)
        print(f"Moving by {dist} ({self.top.rect.left})")
