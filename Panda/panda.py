#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    import pygame
except ImportError:
    print "Problem with import pygame module."
    print "sudo apt-get install python-pygame "

try:
    import numpy as np
except ImportError:
    print "Problem with import numpy module."
    print "sudo apt-get install python-numpy"

import os


class Panda(object):

    def __init__(self, game):
        self.current_path = os.path.dirname(__file__)
        self.resource_path = os.path.join(self.current_path, 'pictures')
        self.game = game
        self.speed = 1.3
        self.gravity = 0.5
        self.filename = self.resource_path + '/panda.png'

        self.pos = np.array([0.0,0.0])
        self.vel = np.array([0.0,0.0])
        self.acc = np.array([0.0,0.0])

        try:
            self.sheet = pygame.image.load(self.filename).convert_alpha()
        except pygame.error, message:
            print 'Unable to load spritesheet image:', self.filename
            raise SystemExit, message

        self.size = self.sheet.get_rect().size

    def add_force(self, force):
        self.acc += force

    def tick(self):
        #Bounaries:
        pressed = pygame.key.get_pressed()
        if self.pos[1] >= 560:
            self.add_force([0, -self.gravity])

        if self.game.move == True:
            if (pressed[pygame.K_w] or pressed[pygame.K_UP]) and self.pos[1] <= 0:
                self.add_force([0, self.speed])
            if (pressed[pygame.K_s] or pressed[pygame.K_DOWN]) and self.pos[1] >= 580:
                self.add_force([0, -self.speed])
            if (pressed[pygame.K_a] or pressed[pygame.K_LEFT]) and self.pos[0] <= 0:
                self.add_force([self.speed, 0])
            if (pressed[pygame.K_d] or pressed[pygame.K_RIGHT]) and self.pos[0] >= 1160 :
                self.add_force([-self.speed, 0])

            if pressed[pygame.K_w] or pressed[pygame.K_UP]:
                self.add_force([0,-self.speed])
            if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
                self.add_force([0, self.speed])
            if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
                self.add_force([-self.speed, 0])
            if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
                self.add_force([self.speed, 0])
            # Physics
            self.vel *= 0.8
            self.vel -= [0,-self.gravity]

            self.vel += self.acc
            self.pos += self.vel
            self.acc *= 0
        else:
            if self.game.seconds_szustak - self.game.randtimeszustak > 0:
                self.rest_time = str(self.game.seconds_szustak - self.game.randtimeszustak)
            elif self.game.seconds_szustak - self.game.randtimeszustak < 0:
                self.rest_time = str(self.game.seconds_szustak + self.game.randtimeszustak)
            self.game.screen.blit(self.game.myfont.render(self.rest_time, True, (255, 0, 0)), (self.game.szustak.pos[0] + self.game.szustak.size[0]/2, self.game.szustak.pos[1]))

            pygame.display.update()

    def draw(self):
        self.game.screen.blit(self.sheet, (self.pos[0], self.pos[1]))
