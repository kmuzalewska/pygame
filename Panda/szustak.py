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


import random
import os

class Szustak(object):
    def __init__(self, game):
        self.current_path = os.path.dirname(__file__)
        self.resource_path = os.path.join(self.current_path, 'pictures')
        self.game = game
        self.filename = self.resource_path + '/szustak.png'
        # print self.filename
        self.pos = np.array([random.uniform(0, 1160), random.uniform(0, 480)])
        try:
            self.sheet = pygame.image.load(self.filename).convert_alpha()
        except pygame.error, message:
            print 'Unable to load spritesheet image:', self.filename
            raise SystemExit, message

        self.size = self.sheet.get_rect().size

    def draw(self):
        self.game.screen.blit(self.sheet, (self.pos[0], self.pos[1]))

    def collision(self):
        if self.game.detectCollision(self):
            self.game.move = False
