# program file for Player movement and bullets
#criated by Vitor Daniel, nº a22204782 and João Carvalho, nº a22204909

import pygame
import math
import numpy as np


#colors
white = (255, 255, 255)
black = (0, 0, 0)

red = 0
green = 0
blue = 0

#"rainbow" color
ang= ang + np.pi/360
red=(math.cos(ang)+1)/2*255
blue=(math.sin(ang)+1)/2*255
green=((math.cos(ang))*(math.sin(ang))+1)/2*255
Color=(red, green, blue)

#screen size
Window_width = 800
Window_height = 600

#draw screen
# Make surface and display
Window = pygame.display.set_mode((Window_width, Window_height))
pygame.display.set_caption("Asteroids")

class Player:
    def __init__(self):



class Bullet:
    
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.dir = direction

    def updateBullet(self):
            #movement
            self.x += bullet_speed * math.cos(self.dir * math.pi / 180)
            self.y += bullet_speed * math.sin(self.dir * math.pi / 180)

            #draw bullet
            pygame.draw.circle(Window, white, (int(self.x), int(self.y)), 3)

            #fit in screen
            if self.x > Window_width:
                self.x = 0
            elif self.x < 0:
                self.x = Window_width
            elif self.y > Window_height:
                self.y = 0
            elif self.y < 0:
                self.y = Window_height
            self.life -= 1


