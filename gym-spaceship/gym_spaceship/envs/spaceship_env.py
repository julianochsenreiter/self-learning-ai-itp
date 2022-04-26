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
        # init env
        self.action_space = spaces.Discrete(2)

        self.observation_space = spaces.Dict(
            {
                "ship": spaces.Discrete(2),
                "top": spaces.Discrete(1),
                "bottom": spaces.Discrete(1)
            }
        )

        # init pygame
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("A.I.M.")

        self.score = 0
        self.obstacles = []
        self.ship = Ship()

    def step(self, action):
        self.screen.fill(BACKGROUND)
        shiprect = self.ship.draw()

        if(action == 0): # UP
            self.ship.up(10)
        elif(action == 1):
            self.ship.down(10)

        if len(self.obstacles) < 4 and canAddObstacle(self.obstacles):
            self.obstacles.append(obstacle.Obstacle(self.screen, spawndist))
        for o in self.obstacles:
            if o.isTouching(shiprect):
                self.restart()
            
            if o.xpos < minpos:
                self.obstacles.remove(o)
                score += 1
            o.draw()
            o.move(20)
        
    def reset(self, seed=None):
        super().reset(seed = seed)

        return self.getObs()
        
    def render(self, mode='human'):
        for o in self.obstacles:
            o.draw()

    def close(self):
        # TODO
        pass

    def getObs(self):
        o = self.obstacles[0]
        return {
            "ship": self.ship.position, 
            "top": o.top.bottomleft, 
            "bottom": o.bottom.bottomleft
        }

# utils

width = 800
height = 600
BACKGROUND = (20, 20, 20)
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

spawndist = getWidth(1+(obstacle.hgap*2))