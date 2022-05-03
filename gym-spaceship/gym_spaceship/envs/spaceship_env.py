from typing import Tuple
import random

import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np

import pygame
from pygame.sprite import Sprite
from pygame.surface import Surface

# https://www.gymlibrary.ml/

class SpaceshipEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        # init env
        self.action_space = spaces.Discrete(2)

        self.observation_space = spaces.Dict(
            {
                "ship": spaces.Discrete(height),
                "top": spaces.Discrete(spawndist+abs(minpos)+2),
                "bottom": spaces.Discrete(spawndist+abs(minpos)+2, start=minpos)
            }
        )

        # init pygame
        self.window = None
        self.clock = None

        # init gameplay
        self.obstacles = []
        self.ship = Ship()
        self.score = 0

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
                self.score += 1
            o.move(20)

        obs = self.getObs()
        info = self.getInfo()

        return obs, reward, done, info 
        
    def reset(self, seed=None, return_info=False):
        super().reset(seed = seed)
        self.seed = seed;

        self.obstacles.clear()
        self.ship = Ship()
        self.score = 0

        obs = self.getObs()
        info = self.getInfo()
        # print(f"{obs=} {type(obs)=}")
        return (obs, info) if return_info else obs
        
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
                "ship": self.ship.ypos,
                "top": 0,
                "bottom": 0
            }

        o = self.obstacles[0]
        print(f"{o.top.rect.left=} {o.bottom.rect.left}")
        return {
            "ship": self.ship.ypos, 
            "top": o.top.rect.left,
            "bottom": o.bottom.rect.left
        }
    
    def getInfo(self):
        return {
            "score": self.score
        }
class Ship:
    # speed = 20
    # vertspeed = 200
    # xpos = 10
    # ypos = 50
    # display = pygame.display.set_mode((800,600)) 

    @property
    def position(self):
        return (self.xpos, self.ypos)

    def __init__(self):
        self.speed = 20
        self.vertspeed = 200
        self.xpos = 100
        self.ypos = 50
        self.display = pygame.display.set_mode((800,600))
        # inpos = Sprite()
    
    def up(self, speed: int):
        self.ypos -= speed
        if self.ypos < 10:
            self.ypos = 10
        # print(self.ypos)

    def down(self, speed: int):
        self.ypos += speed
        if self.ypos > 590:
            self.ypos = 590
        # print(self.ypos)

    def draw(self) -> pygame.Rect:
        return pygame.draw.polygon(self.display, color=(255,80,80), points=[(self.xpos, self.ypos+10), (self.xpos+30,self.ypos), (self.xpos,self.ypos-10)])
class Obstacle:
    @property
    def xpos(self):
        return self.top.rect.left

    def __init__(self, x: int, seed : int = None):
        from .spaceship_env import (getWidth, getHeight)
        # generate distance
        if seed != None:
            random.seed(seed)
        topdist = random.random()

        buffer = minheight + hgap
        max = 1 - buffer
        if topdist > max:
            topdist = max
        bottomdist = 1 - topdist - hgap

        #top
        self.top = Sprite()
        self.top.surf = Surface((getWidth(width), getHeight(topdist)))
        self.top.surf.fill(OBSTC)
        self.top.rect = self.top.surf.get_rect()
        self.top.rect.topleft = (x, 0)

        #bottom
        self.bottom = Sprite()
        self.bottom.surf = Surface((getWidth(width), getHeight(bottomdist)))
        self.bottom.surf.fill(OBSTC)
        self.bottom.rect = self.bottom.surf.get_rect()
        self.bottom.rect.topleft = (x, getHeight(1-bottomdist))


        # print(f"Created obstacle at {x} ({self.xpos})")

    def draw(self, surf):
        """draw on surface"""
        surf.blit(self.top.surf,self.top.rect)
        surf.blit(self.bottom.surf, self.bottom.rect)
    
    def move(self, dist: float):
        """Move left a certain distance"""
        self.top.rect.move_ip(-dist, 0)
        self.bottom.rect.move_ip(-dist, 0)
        # print(f"Moving by {dist} ({self.xpos})")
    
    def isTouching(self, r : Tuple[float, float] | pygame.Rect ):
        if isinstance(r, pygame.Rect):
            # check top
            if self.top.rect.colliderect(r):
                return True
            
            # check bottom
            if self.bottom.rect.colliderect(r):
                return True
        elif isinstance(r, tuple):
            if self.top.rect.collidepoint(r):
                return True
            
            if self.bottom.rect.collidepoint(r):
                return True
        else:
            raise ValueError
        
        return False
# utils

width = 800
height = 600
BACKGROUND = (20, 20, 20)
minpos = -100

# All values are % of the screen
# the gap between the top and the bottom pipe
vgap = 0.15

# the gap between the sets of pipes
hgap = 0.25

# the width of the pipes
width = 0.1

# minimum height of the pipes
minheight = 0.1

OBSTC = pygame.Color(225, 255, 225)

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