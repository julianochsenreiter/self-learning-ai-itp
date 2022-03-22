import pygame
from pygame.sprite import Sprite
from pygame.surface import Surface
class Ship:
    speed = 20
    vertspeed = 200
    xpos = 10
    ypos = 50
    display = pygame.display.set_mode((800,600)) 
    d = pygame.draw.polygon(display, color=(255,0,0), points=[(xpos, ypos+10), (xpos+10,ypos), (xpos,ypos-10)])

    def __init__(self):
        self.speed = 20
        self.vertspeed = 200
        self.xpos = 10
        self.ypos = 50
        self.display = pygame.display.set_mode((800,600))
        inpos = Sprite()
    
    def up(self):
        self.ypos -= 50

    def down(self):
        self.ypos += 50       

    def draw(self):
        pygame.draw.polygon(self.display, color=(255,0,0), points=[(self.xpos, self.ypos+15), (self.xpos+35,self.ypos), (self.xpos,self.ypos-15)])  
