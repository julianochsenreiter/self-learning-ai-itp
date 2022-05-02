import random
from typing import Tuple
import pygame
from pygame.surface import Surface
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

OBSTC = pygame.Color(225, 255, 225)
class Obstacle:
    @property
    def xpos(self):
        return self.top.rect.left

    def __init__(self, x: int, seed : int = None):
        from .spaceship_env import (getWidth, getHeight)
        # generate distance
        if seed != None:
            random.seed(seed)
        topdist = random.random()

        buffer = minheight + hgap
        max = 1 - buffer
        if topdist > max:
            topdist = max
        bottomdist = 1 - topdist - hgap

        #top
        self.top = Sprite()
        self.top.surf = Surface((getWidth(width), getHeight(topdist)))
        self.top.surf.fill(OBSTC)
        self.top.rect = self.top.surf.get_rect()
        self.top.rect.topleft = (x, 0)

        #bottom
        self.bottom = Sprite()
        self.bottom.surf = Surface((getWidth(width), getHeight(bottomdist)))
        self.bottom.surf.fill(OBSTC)
        self.bottom.rect = self.bottom.surf.get_rect()
        self.bottom.rect.topleft = (x, getHeight(1-bottomdist))


        # print(f"Created obstacle at {x} ({self.xpos})")

    def draw(self, surf):
        """draw on surface"""
        surf.blit(self.top.surf,self.top.rect)
        surf.blit(self.bottom.surf, self.bottom.rect)
    
    def move(self, dist: float):
        """Move left a certain distance"""
        self.top.rect.move_ip(-dist, 0)
        self.bottom.rect.move_ip(-dist, 0)
        # print(f"Moving by {dist} ({self.xpos})")
    
    def isTouching(self, r : Tuple[float, float] | pygame.Rect ):
        if isinstance(r, pygame.Rect):
            # check top
            if self.top.rect.colliderect(r):
                return True
            
            # check bottom
            if self.bottom.rect.colliderect(r):
                return True
        elif isinstance(r, tuple):
            if self.top.rect.collidepoint(r):
                return True
            
            if self.bottom.rect.collidepoint(r):
                return True
        else:
            raise ValueError
        
        return False
