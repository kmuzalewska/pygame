import pygame
import numpy as np
import random

class Szustak(object):

    def __init__(self, game):
        self.game = game
        self.filename = 'szustak.jpg'

        self.pos = np.array([random.uniform(0,1160), random.uniform(0, 580)])
        try:
            self.sheet = pygame.image.load(self.filename).convert()
        except pygame.error, message:
            print 'Unable to load spritesheet image:', self.filename
            raise SystemExit, message

    def draw(self):
        self.game.screen.blit(self.sheet, (self.pos[0], self.pos[1]))