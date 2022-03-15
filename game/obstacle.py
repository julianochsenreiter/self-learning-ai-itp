import random
import pygame
from pygame.draw import rect

# All values are % of the screen
# the gap between the top and the bottom pipe
vgap = 0.15

# the gap between the sets of pipes
hgap = 0.15

# the width of the pipes
width = 0.1

# minimum height of the pipes
minheight = 0.1

colour = pygame.Color(40, 80, 40)
class Obstacle:
    top = 0
    bottom = 0

    def __init__(kwargs):
        top = random.random()
        buffer = minheight + width
        max = 1 - buffer
        if top > max:
            top = max
        
        bottom = 1 - top - width

    def draw(self, x):
        from main import (getWidth, getHeight)
        # draw top
        topsurf = pygame.Surface((getWidth(width), self.top))
        rect( topsurf, colour, topsurf.get_rect() )

        #draw bottom
        btmsurf = pygame.Surface((getWidth(width), self.bottom))
        rect(btmsurf, colour, btmsurf.get_rect())