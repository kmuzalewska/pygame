import pygame
import numpy as np
import random

class Bambus(object):

    def __init__(self, game):
        self.game = game
        self.filename = 'bambus.png'

        self.pos = np.array([random.uniform(0,1160), random.uniform(0, 580)])
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
            self.game.start_ticks = pygame.time.get_ticks()
            self.game.food = Bambus(self)
            self.game.randtimebabmus = random.randint(1, 10)
            self.game.score+=1
