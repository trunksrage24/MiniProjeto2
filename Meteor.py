import pygame, sys
from pygame.locals import *
import random
from Imports import *
from Menu import *
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

                        meteor.nx8=meteor.nx8-0.1
                        meteor.mudX2=meteor.mudX2+0.1                
                        meteor.mudY6=meteor.mudY6+0.1

                        meteor.nx9= meteor.nx9+0.1
                        meteor.mudX7=meteor.mudX7+0.1

                        meteor.nx12=meteor.nx12+0.1
                        meteor.mudX8=meteor.mudX8+0.1
                        meteor.mudY8=meteor.mudY8+0.3 

                        meteor.nx10=meteor.nx10+0.1
                        meteor.mudX9=meteor.mudX9+0.1
                        meteor.mudY9=meteor.mudY9+0.1  

                        meteor.nx11=meteor.nx11+0.1
                        meteor.mudX10=meteor.mudX10+0.1

                        meteor.nx13=meteor.nx13+0.1
                        meteor.mudY10=meteor.mudY10+0.3

                        meteor.nx14=meteor.nx14+0.1
                        meteor.mudX11=meteor.mudX11+0.1
                        meteor.mudY11=meteor.mudY11+0.1

                        meteor.nx15=meteor.nx15+0.1
                        meteor.mudX12=meteor.mudX12+0.1
                        meteor.mudY12=meteor.mudY12+0.1

                        meteor.nx16=meteor.nx16+0.1
                        meteor.mudX13=meteor.mudX13+0.1
                        meteor.mudY13=meteor.mudY13+0.1

                        meteor.nx17=meteor.nx17+0.1
                        meteor.mudX14=meteor.mudX14+0.1
                        meteor.mudY14=meteor.mudY14+0.1 

                        meteor.nx18=meteor.nx18+0
                        meteor.mudX15=meteor.mudX15+0.1
                       
                        meteor.nx19=meteor.nx19+0.1
                        meteor.mudY15=meteor.mudY15+0.1

                        meteor.nx20=meteor.nx20+0.1
                        meteor.mudX16=meteor.mudX16+0.1
                        meteor.mudY16=meteor.mudY16+0.1

                        meteor.nx21= meteor.nx21+0.1
                        meteor.mudX17=meteor.mudX17+0.1
                        meteor.mudY17=meteor.mudY17+0.1 

                        meteor.nx22=meteor.nx22+0.1
                        meteor.mudX18=meteor.mudX18+0.1
                        meteor.mudY18=meteor.mudY18+0.1 

                        if meteor.auxhp<=0 and meteor.auxsmlhp1!=0:
                                pygame.draw.circle(SCREEN,RED,[meteor.nx5+meteor.mudX4,meteor.nx5+meteor.mudY4],20) 
                                if meteor.nx5+meteor.mudX4>=800 or meteor.nx5+meteor.mudY4>=600:
                                        meteor.nx5=0
                                        meteor.mudX4=0.3
                                        meteor.mudY4=0.3 

                        if meteor.auxhp<=0 and meteor.auxsmlhp2!=0:
                                pygame.draw.circle(SCREEN,RED,[meteor.nx6+meteor.mudX5,meteor.nx6],20)
                                if meteor.nx6+meteor.mudX5>=800 or meteor.nx6>=600:
                                        meteor.nx6=0
                                        meteor.mudX5=0.3
                                        

                        if meteor.auxhp<=0 and meteor.auxsmlhp3!=0:
                                pygame.draw.circle(SCREEN,RED,[meteor.nx7,meteor.nx7+meteor.mudY5],20)
                                if meteor.nx7>=800 or meteor.nx7+meteor.mudY5>=600:
                                        meteor.nx7=0
                                        meteor.mudY5=0.3

                        if meteor.auxhp<=0 and meteor.auxsmlhp4!=0:
                                pygame.draw.circle(SCREEN,RED,[meteor.nx9,meteor.nx9+meteor.mudY7],20)
                                if meteor.nx9>=800 or meteor.nx9+meteor.mudY7<=0:
                                        meteor.nx9=0
                                        meteor.mudX7=0.1


                        #ainda por ser vista                
                        if meteor.auxhp<=0 and meteor.auxsmlhp5!=0:
                                pygame.draw.circle(SCREEN,RED,[meteor.nx8-meteor.mudX2,meteor.nx8],20) 
                                if meteor.nx8-meteor.mudX2<=0 or meteor.nx8>=800:
                                        meteor.nx8=600
                                        meteor.mudX2=0.1
                                        meteor.mudY6=0.1                
                        






                        if meteor.auxhp<=0 and meteor.auxsmlhp6!=0:
                                pygame.draw.circle(SCREEN,RED,[meteor.nx12+meteor.mudX8,meteor.nx12-meteor.mudY8],20)
                                if meteor.nx12+meteor.mudX8>=800 or meteor.nx1-meteor.mudY8>=600:
                                        meteor.nx12=0
                                        meteor.mudX8=0.3
                                        meteor.mudY8=0.3 

                        if meteor.auxhp1<=0 and meteor.auxsmlhp7!=0:
                                pygame.draw.circle(SCREEN,WHITE,[meteor.nx10+meteor.mudX9,meteor.nx10+meteor.mudY9],20) 
                                if meteor.nx10+meteor.mudX9>=800 or meteor.nx10+meteor.mudY9>=600:
                                        meteor.nx10=0
                                        meteor.mudX9=0.3
                                        meteor.mudY9=0.3 

                        if meteor.auxhp1<=0 and meteor.auxsmlhp8!=0:
                                pygame.draw.circle(SCREEN,RED,[meteor.nx11+meteor.mudX10,meteor.nx11],20)
                                if meteor.nx11+meteor.mudX10>=800 or meteor.nx11>=600:
                                        meteor.nx11=0
                                        meteor.mudX10=0.3
                                         
                        if meteor.auxhp1<=0 and meteor.auxsmlhp9!=0:
                                pygame.draw.circle(SCREEN,RED,[meteor.nx13,meteor.nx13+meteor.mudY10],20)
                                if meteor.nx13>=800 or meteor.nx1+meteor.mudY2>=600:
                                        meteor.nx13=0
                                        meteor.mudY10=0.3

                        if meteor.auxhp1<=0 and meteor.auxsmlhp10!=0:
                                pygame.draw.circle(SCREEN,color_dark,[meteor.nx14-meteor.mudX11,meteor.nx14-meteor.mudY11],20)
                                if meteor.nx14-meteor.mudX11>=800 or meteor.nx14-meteor.mudY11>=600:
                                        meteor.nx14=0
                                        meteor.mudX11=0.3
                                        meteor.mudY11=0.3 
                        if meteor.auxhp1<=0 and meteor.auxsmlhp11!=0:
                                pygame.draw.circle(SCREEN,RED,[meteor.nx15-meteor.mudX12,meteor.nx15+meteor.mudY12],20) 
                                if meteor.nx15-meteor.mudX12>=800 or meteor.nx15+meteor.mudY12>=600:
                                        meteor.nx15=0
                                        meteor.mudX12=0.3
                                        meteor.mudY12=0.3
                        if meteor.auxhp1<=0 and meteor.auxsmlhp12!=0:
                                pygame.draw.circle(SCREEN,RED,[meteor.nx16+meteor.mudX13,meteor.nx16-meteor.mudY13],20) 
                                if meteor.nx16+meteor.mudX13>=800 or meteor.nx16-meteor.mudY13>=600:
                                        meteor.nx16=0
                                        meteor.mudX13=0.3
                                        meteor.mudY13=0.3            

                        if meteor.auxhp2<=0 and meteor.auxsmlhp13!=0:
                                pygame.draw.circle(SCREEN,RED,[meteor.nx17+meteor.mudX14,meteor.nx17+meteor.mudY14],20)
                                if meteor.nx17+meteor.mudX14>=800 or meteor.nx17+meteor.mudY14>=600:
                                        meteor.nx17=0
                                        meteor.mudX14=0.3
                                        meteor.mudY14=0.3  
                        if meteor.auxhp2<=0 and meteor.auxsmlhp14!=0:
                                pygame.draw.circle(SCREEN,RED,[meteor.nx18+meteor.mudX15,meteor.nx18],20)
                                if meteor.nx18+meteor.mudX15>=800 or meteor.nx18>=600:
                                        meteor.nx18=0
                                        meteor.mudX15=0.1
                                        
                        if meteor.auxhp2<=0 and meteor.auxsmlhp15!=0:
                                pygame.draw.circle(SCREEN,RED,[meteor.nx19,meteor.nx19+meteor.mudY15],20)
                                if meteor.nx19>=800 or meteor.nx19+meteor.mudY15>=600:
                                        meteor.nx19=0
                                        meteor.mudY15=0.1
                        if meteor.auxhp2<=0 and meteor.auxsmlhp16!=0:
                                pygame.draw.circle(SCREEN,color_dark,[meteor.nx20-meteor.mudX16,meteor.nx20-meteor.mudY16],20)
                                if meteor.nx20-meteor.mudX16 or meteor.nx20-meteor.mudY16>=600:
                                        meteor.nx20=0
                                        meteor.mudX16=0.1
                                        meteor.mudY16=0.1
                        if meteor.auxhp2<=0 and meteor.auxsmlhp17!=0:
                                pygame.draw.circle(SCREEN,RED,[meteor.nx21-meteor.mudX17,meteor.nx21+meteor.mudY17],20)
                                if meteor.nx21-meteor.mudX17 or meteor.nx21+meteor.mudY17>=600:
                                        meteor.nx21=0
                                        meteor.mudX17=0.1
                                        meteor.mudY17=0.1 
                        if meteor.auxhp2<=0 and meteor.auxsmlhp18!=0:
                                pygame.draw.circle(SCREEN,RED,[meteor.nx22+meteor.mudX18,meteor.nx22-meteor.mudY18],20)
                                if meteor.nx22+meteor.mudX18 or meteor.nx22-meteor.mudY18>=600:
                                        meteor.nx22=0
                                        meteor.mudX18=0.1
                                        meteor.mudY18=0.1    
                        
                        
while True:  
        for event in pygame.event.get():
        #posição do mouse    
                if event.type==pygame.MOUSEMOTION:
                        #posição do mouse    
                        pos=pygame.mouse.get_pos() 

        SCREEN.fill((0,200,200))
        
        
        

        spawnmeteor()


        pygame.display.update()                