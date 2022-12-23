import pygame, sys
from pygame.locals import *
from Imports import *
from Menu import *
from Player import *
pygame.init()
if meteor.auvar==False:           
    Menufunc()
else:    
    Player()