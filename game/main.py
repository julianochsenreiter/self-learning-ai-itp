from time import sleep
import pygame
import obstacle
from ship import Ship
from pygame.locals import (
    QUIT,
    KEYDOWN
)
from random import randint

width = 800
height = 600

BACKGROUND = (20, 20, 20)

def getHeight(percent):
    return height * percent

def getWidth(percent):
    return width * percent

def main():
    # init pygame
    pygame.init()

    screen = pygame.display.set_mode((width, height))

    run = True
    ship = Ship()
    ship.draw()
    obstacles = [obstacle.Obstacle(screen, 700), obstacle.Obstacle(screen, 1100), obstacle.Obstacle(screen, 1300)]
    for o in obstacles:
        print(f"obs: {o.xpos}")
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    ship.down()
                elif event.key == pygame.K_UP:
                    ship.up()

        screen.fill(BACKGROUND)

        # print(f"Obstacles: {len(obstacles)}")
        for o in obstacles:
            if o.xpos < -100:
                obstacles.remove(o)
                del o
                continue

            o.move(1)
            o.draw()
        
        pygame.display.flip()


if __name__ == "__main__":
    main()
