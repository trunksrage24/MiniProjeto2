import pygame, sys
from pygame.locals import *
from Imports import *
from Menu import *
from Player import *
pygame.init()
#if para quando se carregar no butão start irá passar para o proximo ecra(não funcional)
if meteor.auvar==False:           
    Menufunc()
else:    
    Player()