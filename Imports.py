#criated by Vitor Daniel, nº a22204782 and João Carvalho, nº a22204909

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
    mudX1=0.3
    mudX2=0.3
    mudX3=0.3
    mudX4=0.5
    mudX5=0.1
    mudX6=0.3
    mudX7=0.3
    mudX8=0.3
    mudX9=0.5
    mudX10=0.1
    mudX11=0.3
    mudX12=0.3
    mudX13=0.3
    mudX14=0.5
    mudX15=0.1
    mudX16=0.3
    mudX17=0.3
    mudX18=0.3
    mudX19=0.5

    mudY=0.1
    mudY1=0.3
    mudY2=0.3
    mudY3=0.3
    mudY4=0.5
    mudY5=0.5
    mudY6=0.5
    mudY7=0.5
    mudY8=0.5
    mudY9=0.1
    mudY10=0.3
    mudY11=0.3
    mudY12=0.3
    mudY13=0.5
    mudY14=0.5
    mudY15=0.5
    mudY16=0.5
    mudY17=0.5
    mudY18=0.1

   
    
    destroyed=False

    nx1=0
    nx2=0
    nx3=0
    nx4=0
    nx5=0
    nx6=0
    nx7=0           
    nx8=0
    nx9=0
    nx10=0
    nx11=0
    nx12=0
    nx13=0
    nx14=0
    nx15=0
    nx16=0
    nx17=0
    nx18=0
    nx19=0
    nx20=0
    nx21=0
    nx22=0
    nx22=0

    #medium meteores hp
    auxhp=40
    auxhp1=40
    auxhp2=40
    #small meteores hp
    auxsmlhp1=10
    auxsmlhp2=10
    auxsmlhp3=10
    auxsmlhp4=10
    auxsmlhp5=10
    auxsmlhp6=10

    auxsmlhp7=10
    auxsmlhp8=10
    auxsmlhp9=10
    auxsmlhp10=10
    auxsmlhp11=10
    auxsmlhp12=10

    auxsmlhp13=10
    auxsmlhp14=10
    auxsmlhp15=10
    auxsmlhp16=10
    auxsmlhp17=10
    auxsmlhp18=10

    #big meteor hp
    hp1=100

    def addpoints(self):
        #super().__init__(position, load_sprite("asteroid"), (0, 0))
        #add points aqui
        print("Add points")