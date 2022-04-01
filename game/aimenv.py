import gym
from gym import error, spaces, utils
from gym.utils import seeding

from ship import Ship
import obstacle
import pygame

class AIMEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
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

            )  

    def step(self, action):
        self.screen.fill(BACKGROUND)
        shiprect = ship.draw()

        if len(self.obstacles) < 4 and canAddObstacle(obstacles):
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
            o.move(20
        
    def reset(self):
        # TODO
        pass
        
    def render(self, mode='human'):
        # TODO
        pass

    def close(self):
        # TODO
        pass

    # utils
    
    width = 800
    height = 600
    BACKGROUND = (20, 20, 20)
    spawndist = AIMEnv.getWidth(1+(obstacle.hgap*2))
    minpos = -100

    @staticmethod
    def getHeight(percent):
        return height * percent

    @staticmethod
    def getWidth(percent):
        return width * percent

    @staticmethod
    def obstacleDist():
        return getWidth(obstacle.hgap)
    
    @staticmethod
    def canAddObstacle(list):
        for e in list:
            if isinstance(e, obstacle.Obstacle):
                if e.xpos > obstacleDist():
                    return False
        return True