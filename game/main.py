import pygame
from Ship import Ship
from pygame.locals import (
    QUIT,
    KEYDOWN
)
# init pygame
pygame.init()
ship = Ship()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))

run = True;
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                ship.down()
            elif event.key == pygame.K_UP:
                ship.up()