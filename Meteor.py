import pygame, sys
from pygame.locals import *
import random
from Imports import *

pygame.init()

x=0
y=0
    
def spawnmeteor():
        if meteor.destroyed==False:
                meteor.nx1=random.uniform(0.1,500)

                pygame.draw.circle(SCREEN,color_dark,[meteor.nx1,0],20)
                meteor.destroyed=True
        elif meteor.destroyed==True:
                #big asteroid
                meteor.mudX=meteor.mudX+0.1
                meteor.mudY=meteor.mudY+0.1  
                if meteor.hp1>0:
                        meteor.nx2=meteor.nx1
                        meteor.nx3=meteor.nx1
                        meteor.nx4=meteor.nx1
                        meteor.nx5=meteor.nx1
                        meteor.nx6=meteor.nx1
                        meteor.nx7=meteor.nx1
                        meteor.nx8=meteor.nx1
                        meteor.nx9=meteor.nx1
                        meteor.nx10=meteor.nx1
                        meteor.nx11=meteor.nx1
                        meteor.nx12=meteor.nx1
                        meteor.nx13=meteor.nx1  
                        pygame.draw.circle(SCREEN,color_dark,[meteor.nx1+meteor.mudX,meteor.nx1+meteor.mudY],60)    
                        if meteor.nx1+meteor.mudX>=800 or meteor.nx1+meteor.mudY>=600:
                                meteor.nx1=0
                                meteor.mudX=0
                                meteor.mudY=0
                if meteor.hp1==0:
                        meteor.mudX1=meteor.mudX1+0.1
                        meteor.mudY1=meteor.mudY1+0.1
                        meteor.mudX2=meteor.mudX2+0.1
                        meteor.mudY2=meteor.mudY2+0.1 
                        #medium asteroids
                        if meteor.auxhp>0:
                                pygame.draw.circle(SCREEN,color_shade,[meteor.nx2+meteor.mudX1,meteor.nx2],40)
                                if meteor.nx2+meteor.mudX1>=800 or meteor.nx2>=600:
                                        meteor.nx2=0
                                        meteor.mudX1=0      
                        if meteor.auxhp1>0:        
                                pygame.draw.circle(SCREEN,RED,[meteor.nx3+meteor.mudX2,meteor.nx3+meteor.mudX2],40)
                                if meteor.nx3+meteor.mudX2>=800 or meteor.nx3+meteor.mudX2>=600:
                                        meteor.nx3=0
                                        meteor.mudX2=0      
                        if meteor.auxhp2>=0:        
                                pygame.draw.circle(SCREEN,color_dark,[meteor.nx4+meteor.mudX3,meteor.nx4+meteor.mudY2],40)
                                if meteor.nx4+meteor.mudX3>=800 or meteor.nx4+meteor.mudY2>=600:
                                        meteor.nx4=0
                                        meteor.mudX3=0.3
                                        meteor.mudY2=0.3
                        #small asteroids
                        meteor.nx5=meteor.nx5+0.1
                        meteor.mudX4=meteor.mudX4+0.1
                        meteor.mudY4=meteor.mudX4+0.1
                        meteor.nx6=meteor.nx6+0.1
                        meteor.mudX5=meteor.mudX5+0.1
                        meteor.nx7=meteor.nx7+0.1
                        meteor.mudY5=meteor.mudY5+0.1 
                
        pygame.draw.circle(screen,color_dark,[x,y],20)

        pygame.display.update()                