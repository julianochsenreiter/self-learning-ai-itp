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
import os

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

def readScore() -> int:
    print(os.getcwd())
    with open("highscore.csv") as file:
        content = file.read()
        if content == "":
            return 0
        else:
            return int(content)

def writeScore(score: int):
    with open("highscore.csv","w") as file:
        file.write(str(score))

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

    scr = os.path.dirname(__file__)
    os.chdir(scr)

    highscore = readScore()
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
        shiprect = ship.draw()

        if len(obstacles) < 4 and canAddObstacle(obstacles):
            obstacles.append(obstacle.Obstacle(screen, spawndist))
        for o in obstacles:
            if o.isTouching(shiprect):
                restart()
                score = 0
            
            if o.xpos < minpos:
                obstacles.remove(o)
                score += 1
                if score > highscore:
                    highscore = score
                    writeScore(score)
            o.draw()
            o.move(20)  
        
        scoresurf = font.render(f"Score: {score}", False, (200,200,0))
        screen.blit(scoresurf, (10,10))
        
        scoresurf = font.render(f"Highscore: {highscore}", False, (200,200,0))
        screen.blit(scoresurf, (180,10))
        
        pygame.display.flip()
        fpsClock.tick(FPS)

def restart():
    ship = Ship()
    obstacles.clear()

if __name__ == "__main__":
    main()
    