import gym
from gym import error, spaces, utils
from gym.utils import seeding

from ship import Ship
import obstacle
import pygame

# https://www.gymlibrary.ml/

class SpaceshipEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        # init pygame
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("A.I.M.")

        self.score = 0
        self.obstacles = []

    def step(self, action):
        self.screen.fill(BACKGROUND)
        shiprect = ship.draw()

        if len(self.obstacles) < 4 and canAddObstacle(self.obstacles):
            self.obstacles.append(obstacle.Obstacle(self.screen, spawndist))
        for o in self.obstacles:
            if o.isTouching(shiprect):
                restart()
                
            
            if o.xpos < minpos:
                obstacles.remove(o)
                score += 1
                if score > highscore:
                    highscore = score
                    writeScore(score)
            o.draw()
            o.move(20)
        
    def reset(self):
        score = 0
        
    def render(self, mode='human'):
        # TODO
        pass

    def close(self):
        # TODO
        pass

ACTION_LOOKUP = {
    0, #up
    1 #down
}

# utils

width = 800
height = 600
BACKGROUND = (20, 20, 20)
spawndist = getWidth(1+(obstacle.hgap*2))
minpos = -100

def getHeight(percent):
    return height * percent

def getWidth(percent):
    return width * percent

def obstacleDist():
    return getWidth(obstacle.hgap)

def canAddObstacle(list):
    for e in list:
        if isinstance(e, obstacle.Obstacle):
            if e.xpos > obstacleDist():
                return False
    return True