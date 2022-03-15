import random
import pygame
from pygame.draw import rect

# All values are % of the screen
# the gap between the top and the bottom pipe
vgap = 0.15

# the gap between the sets of pipes
hgap = 0.25

# the width of the pipes
width = 0.1

# minimum height of the pipes
minheight = 0.1

colour = pygame.Color(40, 80, 40)
class Obstacle:
    top = 0
    bottom = 0

    def __init__(self):
        self.top = random.random()
        buffer = minheight + hgap
        max = 1 - buffer
        if self.top > max:
            self.top = max
        
        self.bottom = 1 - self.top - hgap

    def draw(self, surf: pygame.Surface, x: int):
        from main import (getWidth, getHeight)
        # draw top
        topsurf = pygame.Surface((getWidth(width), getHeight(self.top)))
        topsurf.fill(colour)

        #draw bottom
        btmsurf = pygame.Surface((getWidth(width), getHeight(self.bottom)))
        btmsurf.fill(colour)

        surf.blit(topsurf, (x, 0) )
        surf.blit(btmsurf, (x, getHeight(1-self.bottom)))
        pygame.display.flip()