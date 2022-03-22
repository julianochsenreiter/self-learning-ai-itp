import pygame
class Ship:
    speed = 20
    vertspeed = 200
    xpos = 10
    ypos = 50
    display = pygame.display.set_mode((800,600))

    def __init__(self):
        self.speed = 20
        self.vertspeed = 200
        self.xpos = 10
        self.ypos = 50
        self.display = pygame.display.set_mode((800,600))
    
    def up(self):
        self.ypos += 5

    def down(self):
        self.ypos -= 5

    def draw(self):
        pygame.draw.polygon(self.display, color=(255,0,0), points=[(5,55), (15,50), (5,45)])   
