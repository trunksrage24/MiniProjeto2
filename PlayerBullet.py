# program file for Player Movement and Bullets
#criated by Vitor Daniel, nº a22204782 and João Carvalho, nº a22204909

#fetch libraries from Imports, where all libraries needed are stored
from Imports import *

window_width = SCREEN.get_width

#colors
white = (255, 255, 255)
black = (0, 0, 0)

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

#player variables
playerSpeed = 10
playerMaxSpeed = 20
playerMaxRotation = 10
playerColor = white
playerSize = 10

class Player:
    
        # Check for wrapping
        if self.x > display_width:
            self.x = 0
        elif self.x < 0:
            self.x = display_width
        elif self.y > display_height:
            self.y = 0
        elif self.y < 0:
            self.y = display_height

        # Rotate player
        self.dir += self.rtspd

    def drawPlayer(self):
        ang = math.radians(self.dir)
        t = self.thrust
        # Draw player
        PLAYER = pygame.image.load("Images/Spaceship.png")
        PLAYER_x = self.x
        PLAYER_y = self.y
        

#player needs image and movement (adapt any good ideas from this code above)

#bullet variables
bulletSpeed = 10
bulletColor = Color

class Bullet:
    
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.dir = direction
        self.life = 10

    def Bullet_Fired(self):
            #movement
            self.x += bulletSpeed * math.cos(self.dir * math.pi / 180)
            self.y += bulletSpeed * math.sin(self.dir * math.pi / 180)

            #draw bullet
            pygame.draw.circle(Window, bulletColor, (int(self.x), int(self.y)), 4)

            #fit in screen
            if self.x > Window_width:
                self.x = 0
            elif self.x < 0:
                self.x = Window_width
            elif self.y > Window_height:
                self.y = 0
            elif self.y < 0:
                self.y = Window_height
            self.life -= 1


