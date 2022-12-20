# program file for Player Movement and Bullets
#criated by Vitor Daniel, nº a22204782 and João Carvalho, nº a22204909

import pygame
import math
import numpy as np

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

#keep rainbow looping
if (red > 255):
    red = 0

if (green > 255):
    green = 0

if (blue > 255):
    blue = 0

#screen size
Window_width = 800
Window_height = 600

#draw screen
Window = pygame.display.set_mode((Window_width, Window_height))
pygame.display.set_caption("Asteroids")

playerSpeed = 15
playerMaxSpeed = 20
playerMaxRotation = 10
playerColor = white
playerSize = 10

class Player:
    #adapt code  to my own specifications and requirements, add images
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hspeed = 0
        self.vspeed = 0
        self.dir = -90
        self.rtspd = 0
        self.thrust = False

    def updatePlayer(self):
        # Move player
        speed = math.sqrt(self.hspeed**2 + self.vspeed**2)
        if self.thrust:
            if speed + fd_fric < player_max_speed:
                self.hspeed += fd_fric * math.cos(self.dir * math.pi / 180)
                self.vspeed += fd_fric * math.sin(self.dir * math.pi / 180)
            else:
                self.hspeed = player_max_speed * math.cos(self.dir * math.pi / 180)
                self.vspeed = player_max_speed * math.sin(self.dir * math.pi / 180)
        else:
            if speed - bd_fric > 0:
                change_in_hspeed = (bd_fric * math.cos(self.vspeed / self.hspeed))
                change_in_vspeed = (bd_fric * math.sin(self.vspeed / self.hspeed))
                if self.hspeed != 0:
                    if change_in_hspeed / abs(change_in_hspeed) == self.hspeed / abs(self.hspeed):
                        self.hspeed -= change_in_hspeed
                    else:
                        self.hspeed += change_in_hspeed
                if self.vspeed != 0:
                    if change_in_vspeed / abs(change_in_vspeed) == self.vspeed / abs(self.vspeed):
                        self.vspeed -= change_in_vspeed
                    else:
                        self.vspeed += change_in_vspeed
            else:
                self.hspeed = 0
                self.vspeed = 0
        self.x += self.hspeed
        self.y += self.vspeed

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
        a = math.radians(self.dir)
        x = self.x
        y = self.y
        s = player_size
        t = self.thrust
        # Draw player
        pygame.draw.line(Window, white,
                         (x - (s * math.sqrt(130) / 12) * math.cos(math.atan(7 / 9) + a),
                          y - (s * math.sqrt(130) / 12) * math.sin(math.atan(7 / 9) + a)),
                         (x + s * math.cos(a), y + s * math.sin(a)))

        pygame.draw.line(Window, white,
                         (x - (s * math.sqrt(130) / 12) * math.cos(math.atan(7 / 9) - a),
                          y + (s * math.sqrt(130) / 12) * math.sin(math.atan(7 / 9) - a)),
                         (x + s * math.cos(a), y + s * math.sin(a)))

        pygame.draw.line(Window, white,
                         (x - (s * math.sqrt(2) / 2) * math.cos(a + math.pi / 4),
                          y - (s * math.sqrt(2) / 2) * math.sin(a + math.pi / 4)),
                         (x - (s * math.sqrt(2) / 2) * math.cos(-a + math.pi / 4),
                          y + (s * math.sqrt(2) / 2) * math.sin(-a + math.pi / 4)))
        if t:
            pygame.draw.line(Window, white,
                             (x - s * math.cos(a),
                              y - s * math.sin(a)),
                             (x - (s * math.sqrt(5) / 4) * math.cos(a + math.pi / 6),
                              y - (s * math.sqrt(5) / 4) * math.sin(a + math.pi / 6)))
            pygame.draw.line(Window, white,
                             (x - s * math.cos(-a),
                              y + s * math.sin(-a)),
                             (x - (s * math.sqrt(5) / 4) * math.cos(-a + math.pi / 6),
                              y + (s * math.sqrt(5) / 4) * math.sin(-a + math.pi / 6)))

    def killPlayer(self):
        # Reset the player
        self.x = display_width / 2
        self.y = display_height / 2
        self.thrust = False
        self.dir = -90
        self.hspeed = 0
        self.vspeed = 0

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


