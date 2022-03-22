import pygame
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
        self.d = pygame.draw.polygon(self.display, color=(255,0,0), points=[(self.xpos, self.ypos+10), (self.xpos+10,self.ypos), (self.xpos,self.ypos-10)])
    
    def up(self):
        self.ypos += 5
        self.d.move(0, 5)

    def down(self):
        self.ypos -= 5
        self.d.move(0, -5)
        

    def draw(self):
        self.d = pygame.draw.polygon(self.display, color=(255,0,0), points=[(self.xpos, self.ypos+10), (self.xpos+10,self.ypos), (self.xpos,self.ypos-10)])  
        pygame.display.update() 
