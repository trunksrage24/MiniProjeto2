import pygame, sys
from pygame.locals import *
import random
from Imports import *
from Meteor import *
pygame.init()


def outofscreen(c):            
    if c>=screen.x or c<=(0,0):
        n1=random.uniform(0.1,550)
        meteor.x=5
        meteor.y=5
        if n1<=230:
            meteor.mudX=n1
            meteor.mudY=5
            print(meteor.mudX,meteor.mudY)
        else:        
            meteor.mudX=5
            meteor.mudY=n1
            print(meteor.mudX,meteor.mudY)
def Menufunc(): 
        while True:  
                for event in pygame.event.get():
                        #posição do mouse    
                        if event.type==pygame.MOUSEMOTION:
                                #posição do mouse    
                                pos=pygame.mouse.get_pos()    
                                

                                #start button
                                if start_but.collidepoint(pos):
                                        
                                        pygame.draw.rect(SCREEN,WHITE,(305,200,190,70))
                                        SCREEN.blit(textstart,(350,215))
                                        pygame.display.update()
                                        if pygame.mouse.get_pressed()[0] and start_but.collidepoint(pos):
                                                print("Move on")
                                                spawnmeteor()
                                                break
                                        
                                #exit button
                                if exit_but.collidepoint(pos):
                                        SCREEN.blit(textquit,(350,335))
                                        pygame.draw.rect(SCREEN,WHITE,(305,320,190,70))
                                        pygame.display.update()
                                        if pygame.mouse.get_pressed()[0] and exit_but.collidepoint(pos):
                                                SCREEN.blit(textquit,(350,335))
                                                print("quit")
                                                pygame.quit()   
                                                sys.exit()
                        
                SCREEN.fill((0,0,0)) 
                meteor.x=meteor.x+0.1
                meteor.y=meteor.y+0.1
                pygame.draw.circle(SCREEN,WHITE,[180,230],3)
                pygame.draw.circle(SCREEN,WHITE,[400,120],2)
                pygame.draw.circle(SCREEN,WHITE,[550,500],6)
                pygame.draw.circle(SCREEN,WHITE,[240,300],6)
                pygame.draw.circle(SCREEN,WHITE,[300,123],2)
                pygame.draw.circle(SCREEN,WHITE,[420,320],6)
                pygame.draw.circle(SCREEN,WHITE,[600,12],5)
                pygame.draw.circle(SCREEN,WHITE,[760,34],2)
                pygame.draw.circle(SCREEN,WHITE,[500,532],2) 
                pygame.draw.circle(SCREEN,WHITE,[70,120],5)
                pygame.draw.circle(SCREEN,WHITE,[600,200],5)
                pygame.draw.circle(SCREEN,WHITE,[760,400],2)
                pygame.draw.circle(SCREEN,WHITE,[160,532],7)

                                #METEORITOS NO SCREEN
                pygame.draw.circle(SCREEN,color_dark,[meteor.x+meteor.mudX,meteor.y+meteor.mudY],20)
                c=(meteor.x,meteor.y)
                outofscreen(c)
                pygame.draw.circle(SCREEN,color_dark,[meteor.x-meteor.mudX,meteor.y-meteor.mudY],25)
                c=(meteor.x,meteor.y)
                outofscreen(c)
                pygame.draw.circle(SCREEN,color_dark,[meteor.y+meteor.mudX,meteor.x-meteor.mudY],13)
                c=(meteor.x,meteor.y)
                outofscreen(c)

                                #meteores
                pygame.draw.rect(SCREEN,color_shade,(270,50,260,100))
                pygame.draw.circle(SCREEN,color_dark,[310,85],10)
                pygame.draw.circle(SCREEN,color_dark,[485,115],30)
                SCREEN.blit(textComets,(310,80))
                                
                                #startbutton
                pygame.draw.rect(SCREEN,color_shade,(305,200,190,70))
                SCREEN.blit(textstart,(350,215))
                                #exitbut
                pygame.draw.rect(SCREEN,color_shade,(305,320,190,70))
                SCREEN.blit(textquit,(350,335))      

                pygame.display.update()

