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

class Bambus(object):

    def __init__(self, game):
        self.current_path = os.path.dirname(__file__)
        self.resource_path = os.path.join(self.current_path, 'pictures')
        self.game = game
        self.filename = self.resource_path + '/bambus.png'

        self.pos = np.array([random.uniform(0,1000), random.uniform(0, 450)])
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
            self.game.start_ticks_food = pygame.time.get_ticks()
            self.game.food = Bambus(self.game)
            self.game.randtimebabmus = random.randint(1, 10)
            self.game.score+=1
