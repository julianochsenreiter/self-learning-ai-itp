import pygame
class Ship:
    speed = 20
    vertspeed = 200
    xpos = 10
    ypos = 50
    
    def up():
        ypos += 5

    def down():
        ypos -= 5

    def draw():
        pygame.draw.polygone(pygame.display, color=(255,0,0), points=[(5,55), (15,50), (5,45)])   
