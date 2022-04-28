import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np

from .ship import Ship
from .obstacle import *
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
        self.window = None
        self.clock = None

        self.obstacles = []
        self.ship = Ship()

    def step(self, action):
        done = False
        reward = 0

        if(action == 0): # UP
            self.ship.up(10)
        elif(action == 1): # DOWN
            self.ship.down(10)

        if len(self.obstacles) < 4 and canAddObstacle(self.obstacles):
            if self.seed != None and isinstance(self.seed):
                self.obstacles.append(Obstacle(spawndist, self.seed))
                
            else:
                self.obstacles.append(Obstacle(spawndist))
        
        for o in self.obstacles:
            if o.isTouching(self.ship.position):
                done = True
            if o.xpos < minpos:
                self.obstacles.remove(o)
                reward += 1
            o.draw()
            o.move(20)

        obs = self.getObs()

        return obs, reward, done
        
    def reset(self, seed=None):
        super().reset(seed = seed)
        self.seed = seed;

        obs = self.getObs()
        return obs
        
    def render(self, mode='human'):
        if self.window is None and mode == "human":
            pygame.init()
            pygame.display.init()
            pygame.display.set_caption("Spaceship")
            self.window = pygame.display.set_mode((width, height))

        if self.clock is None and mode == "human":
            self.clock = pygame.time.Clock()

        canvas = pygame.Surface((width, height))
        canvas.fill(pygame.Color)
        for o in self.obstacles:
            o.draw(canvas)
        
        if mode == "human":
            # The following line copies our drawings from `canvas` to the visible window
            self.window.blit(canvas, canvas.get_rect())
            pygame.event.pump()
            pygame.display.update()

            # We need to ensure that human-rendering occurs at the predefined framerate.
            # The following line will automatically add a delay to keep the framerate stable.
            self.clock.tick(self.metadata["render_fps"])
        else:  # rgb_array
            return np.transpose(
                np.array(pygame.surfarray.pixels3d(canvas)), axes=(1, 0, 2)
            )

    def close(self):
        if self.window is not None:
            pygame.display.quit()
            pygame.quit()

    def getObs(self):
        if(len(self.obstacles) == 0):
            return {
                "ship": self.ship.position,
                "top": 0,
                "bottom": 0
            }

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
    return getWidth(hgap)

def canAddObstacle(list):
    for e in list:
        if isinstance(e, Obstacle):
            if e.xpos > obstacleDist():
                return False
    return True

spawndist = getWidth(1+(hgap*2))