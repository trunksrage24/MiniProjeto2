import pygame, sys
from pygame.locals import *
import random
from Imports import *
pygame.init()
x=0
y=0


    
while True:  
        for event in pygame.event.get():
        #posição do mouse    
                if event.type==pygame.MOUSEMOTION:
                        #posição do mouse    
                        pos=pygame.mouse.get_pos() 

        SCREEN.fill((200,200,200))
        
        
        pygame.draw.circle(SCREEN,color_dark,[x,y],20)




        pygame.display.update()                