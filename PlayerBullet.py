# program file for Player Movement and Bullets
#criated by Vitor Daniel, nº a22204782 and João Carvalho, nº a22204909

#fetch libraries from Imports, where all libraries needed are stored
from Imports import *
import numpy as np

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

#rainbow color variables
ang = 0
red = 0
green = 0
blue = 0

#"rainbow" color
ang += np.pi / 360
red = (math.cos(ang) + 1) / 2 * 255
blue = (math.sin(ang) + 1) / 2 * 255
green = ((math.cos(ang)) * (math.sin(ang)) + 1) / 2 * 255
Color = (red, green, blue)

#keep "rainbow" looping
if (red > 255):
    red = 0

if (green > 255):
    green = 0

if (blue > 255):
    blue = 0

#screen
SCREEN.fill(Color)

#player:
#player image
image = pygame.image.load('seta.png')

#coordenadas e angulos
ang = 0
v_pos = [(screen_x / 2), (screen_y / 2)]
v_dir = [-1,-1]
events = pygame.event.get()

#ciclo principal
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_RIGHT:
                v_direcao=[1,0]
            if event.key == pygame.K_LEFT:
                v_direcao=[-1,0]
            if event.key == pygame.K_UP:
                v_direcao=[0,-1]
            if event.key == pygame.K_DOWN:
                v_direcao=[0,1]

    #movimento circle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        v_pos[0]-=4
        print(v_pos)
    if keys[pygame.K_RIGHT]:
        v_pos[0]+=4
        print(v_pos)
    if keys[pygame.K_UP]:
        v_pos[1]-=4
        print(v_pos)
    if keys[pygame.K_DOWN]:
        v_pos[1]+=4
        print(v_pos)
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
    
    #draw
    pygame.draw.line(SCREEN, WHITE, (400, 0), (400, 600), 4)
    pygame.draw.line(SCREEN, WHITE, (0,300), (800,300), 4)
    pygame.draw.line(SCREEN, BLUE, (400,300), v_pos, 4)
    
    cnt_y = SCREEN.get_height()/2
    cnt_x = SCREEN.get_width()/2
    angulo = np.arctan2(cnt_y - v_pos[1], cnt_x - v_pos[0])
    angulo_graus = np.degrees(angulo)
    angulo_graus = np.round(angulo_graus)
    rotimage = pygame.transform.rotate(image,-angulo_graus)
    rect = rotimage.get_rect(center=v_pos)
    SCREEN.blit(rotimage,rect)
    Vetor = str(v_pos)
    Angulo = str(angulo_graus)
    Vpos = (v_pos[0], v_pos[1]+16)
    SCREEN.blit(angle, (Vpos))

    #update do ecra
    pygame.display.update()

#bullet variables
bulletSpeed = 10
bulletColor = Color
bulletTime = 4

class Bullet:
    def fit_screen(self):    
        #fit in screen
        if self.x > screen_x:
            self.x = 0
        elif self.x < 0:
            self.x = screen_x
        elif self.y > screen_y:
            self.y = 0
        elif self.y < 0:
            self.y = screen_y
