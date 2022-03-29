from ast import Delete
from time import sleep
import pygame
import obstacle
from ship import Ship
from pygame.locals import (
    QUIT,
    KEYDOWN
)
from pygame.font import Font
from random import randint

h = open("game/highscore.csv", "r").read()
if h == "":
    h = int(0)
else:
    h = int(h)
f = open("game/highscore.csv", "w")

width = 800
height = 600

FPS = 60
fpsClock = pygame.time.Clock()

BACKGROUND = (20, 20, 20)

def getHeight(percent):
    return height * percent

def getWidth(percent):
    return width * percent

spawndist = getWidth(1+(obstacle.hgap*2))
minpos = -100

def obstacleDist():
    return getWidth(obstacle.hgap)

def canAddObstacle(list):
    for e in list:
        if isinstance(e, obstacle.Obstacle):
            if e.xpos > obstacleDist():
                return False
    return True

ship = Ship()
obstacles = []

def main():
    # init pygame
    pygame.init()
    pygame.font.init()
    
    key = ""
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("A.I.M.")
    font = pygame.font.SysFont("Segue UI", 50)

    run = True
    restart()
    highscore = h
    score = 0
    
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_DOWN:
                    key = "down"
                elif event.key == pygame.K_UP:
                    key = "up"
            if event.type == pygame.KEYUP:
                key = ""
        if key == "up":
            ship.up(20)
        if key == "down":
            ship.down(20)

        screen.fill(BACKGROUND)

        if len(obstacles) < 4 and canAddObstacle(obstacles):
            obstacles.append(obstacle.Obstacle(screen, spawndist))
        for o in obstacles:
            if o.isTouching(ship.xpos, ship.ypos):
                restart()
                score = 0
                

            if o.xpos < minpos:
                obstacles.remove(o)
                score += 1
                if score > highscore:
                    highscore = score
            o.draw()
            # if count % 2 == 0:
            #    o.move(1)
            o.move(20)  
        ship.draw()
        
        scoresurf = font.render(f"Score: {score}", False, (200,200,0))
        screen.blit(scoresurf, (10,10))
        
        scoresurf = font.render(f"Highscore: {highscore}", False, (200,200,0))
        screen.blit(scoresurf, (180,10))
        
        pygame.display.flip()
        fpsClock.tick(FPS)

    if h < highscore:
        f.write(str(highscore))

def restart():
    ship = Ship()
    obstacles.clear()

if __name__ == "__main__":
    main()
    