import pygame
from pygame.locals import *
from Imports import *
from Menu import *
from Player import *
from Leaderboard import *
pygame.init()

#Interstellar Main Theme - Extra Extended - Soundtrack by Hans Zimmer, credits to Cinémavore on Youtube
pygame.mixer.music.load('music.ogg')
pygame.mixer.music.play(-1)


#if para quando se carregar no butão start irá passar para o proximo ecra(não funcional)
if meteor.auvar == False:           
    Menufunc()

else:
    Player(),  Bullet()

