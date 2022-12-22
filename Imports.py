import pygame, sys
from pygame.locals import *
import math
import numpy as np
import random
import time
pygame.init()


SCREEN = pygame.display.set_mode((800, 600))

color_shade = (170,170,170)
color_dark = (100,100,100)
WHITE=(255,255,255)
RED=(255,0,0)
smallfont = pygame.font.SysFont("Corbel",45,True)
textComets = smallfont.render("COMETS" , True , WHITE)
textstart = smallfont.render("Start" , True , RED)
textquit = smallfont.render("Quit" , True , RED)

start_but=pygame.Rect(305,200,190,70)
exit_but=pygame.Rect(305,320,190,70)

class screen:
    x=(800,600)
       
class meteor:
    x=5
    y=5
    mudX=0.1
    mudY=0.1

        
    def addpoints(self):
        #super().__init__(position, load_sprite("asteroid"), (0, 0))
        #add points aqui
        print("Add points")