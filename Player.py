# program file for Player Movement

from Imports import *
from Bullet import *
import numpy as np
import math
import pygame

#configuraçao inicial
pygame.init()
Screen = pygame.display.set_mode((800,600))

#cores
Color1 = 0
Color2 = 0
Color3 = 0
White = (255, 255, 255)
Black = (0, 0, 0)
Yellow = (255, 255, 0)
Aqua = (204, 255, 204)
Orange = (255, 165, 0)
#bullet color
ang = 0
ang = ang + np.pi/2880
Color1 = (math.cos(ang)+1)/2*255
Color2 = (math.sin(ang)+1)/2*255
Color3 = ((math.cos(ang))*(math.sin(ang))+1)/2*255
Rainbow=(Color1, Color2, Color3)

#converte valores para continuar sempre a mudar cor
if (Color1 > 255):
    Color1 = 0
if (Color2 > 255):
    Color2 = 0
if (Color3 > 255):
    Color3 = 0

#imagem
image = pygame.image.load('sprites/image.png')

#coordenadas
v_pos = [400,300]

def Player():
    #ciclo principal
    while True:

        Screen.fill(Black)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        #comandos player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            v_pos[0]-=1
            print(v_pos)
        if keys[pygame.K_RIGHT]:
            v_pos[0]+=1
            print(v_pos)
        if keys[pygame.K_UP]:
            v_pos[1]-=1
            print(v_pos)
        if keys[pygame.K_DOWN]:
            v_pos[1]+=1
            print(v_pos)
        if keys[pygame.K_ESCAPE]:
            pygame.quit()

        #translaçao do player
        cnt_y = Screen.get_height()/2
        cnt_x = Screen.get_width()/2
        angulo = np.arctan2( cnt_y - v_pos[1], cnt_x - v_pos[0])
        angulo_graus=np.degrees(angulo)
        angulo_graus=np.round(angulo_graus)
        rotimage = pygame.transform.rotate(image,-angulo_graus)
        Screen.blit(rotimage, v_pos)

        #update do ecra
        pygame.display.update()
