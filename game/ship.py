import pygame
from pygame.sprite import Sprite
from pygame.surface import Surface
class Ship:
    # speed = 20
    # vertspeed = 200
    # xpos = 10
    # ypos = 50
    # display = pygame.display.set_mode((800,600)) 

    def __init__(self):
        self.speed = 20
        self.vertspeed = 200
        self.xpos = 100
        self.ypos = 50
        self.display = pygame.display.set_mode((800,600))
        # inpos = Sprite()
    
    def up(self):
        self.ypos -= 1
        if self.ypos < 10:
            self.ypos = 10
        # print(self.ypos)

    def down(self):
        self.ypos += 1
        if self.ypos > 590:
            self.ypos = 590
        # print(self.ypos)

    def draw(self):
        pygame.draw.polygon(self.display, color=(255,80,80), points=[(self.xpos, self.ypos+10), (self.xpos+30,self.ypos), (self.xpos,self.ypos-10)])  
