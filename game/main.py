import pygame
import obstacle
from pygame.locals import (
    QUIT,
    KEYDOWN
)

width = 800
height = 600

def getHeight(percent):
    return height * percent

def getWidth(percent):
    return width * percent

def main():
    # init pygame
    pygame.init()

    screen = pygame.display.set_mode((width, height))

    run = True;

    obstacles = [obstacle.Obstacle()]
    while run:
        for event in pygame.event.get():
            if(event.type == QUIT):
                run = False

        for o in obstacles:
            o.draw(100)

if __name__ == "__main__":
    main()