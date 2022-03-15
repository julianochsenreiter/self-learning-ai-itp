import pygame
from pygame.locals import (
    QUIT,
    KEYDOWN
)

# init pygame
pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))

run = True;
while run:
    for event in pygame.event.get():
        if(event.type == QUIT):
            run = False