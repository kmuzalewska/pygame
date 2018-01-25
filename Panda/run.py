#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    import pygame
except ImportError:
    print "Problem with import pygame module."
    print "sudo apt-get install python-pygame "
from panda import Panda
from bambus import Bambus
from szustak import Szustak
import random,sys

class Game(object):
    def __init__(self):
        # Config
        self.tps_max = 100.0
        self.score=3
        self.randtimebabmus = 9
        self.randtimeszustak = 8
        self.move=True
        self.seconds_food = 10
        self.seconds_szustak = 10
        self.pause = False

        # Initialization
        pygame.init()
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 50)
        self.screen = pygame.display.set_mode((1280, 720))
        self.tps_delta = 0.0
        self.start_ticks_food = pygame.time.get_ticks()
        self.start_ticks_szustak = pygame.time.get_ticks()
        self.tps_clock = pygame.time.Clock()

        # Objects
        self.player = Panda(self)
        self.food = None
        self.szustak = None

        # Main loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.pause = True
                    self.paused()

            # Ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max

            if self.szustak:
                self.szustak.collision()
            if self.food:
                self.food.collision()

            # Drawing
            self.screen.fill((10, 200, 0))
            self.draw()
            pygame.display.update()

    def tick(self):
        self.player.tick()
        if self.score <= 0:
            self.gameOver()
        if self.seconds_food == 0:
            self.start_ticks_food = pygame.time.get_ticks()
            self.score -= 1
        if self.seconds_szustak <= 0:
            self.start_ticks_szustak = pygame.time.get_ticks()

    def draw(self):
        # Drawing
        self.seconds_food = 10 - (pygame.time.get_ticks() - self.start_ticks_food) / 1000
        self.seconds_szustak = 10 - (pygame.time.get_ticks() - self.start_ticks_szustak) / 1000
        # print "rand: ", self.randtimeszustak, "second: ", self.seconds_szustak
        if self.seconds_food == self.randtimebabmus:
            self.food = Bambus(self)
            self.randtimebabmus = random.randint(1, 10)
            self.score -= 1
        if self.seconds_szustak == self.randtimeszustak:
            self.szustak = Szustak(self)
            self.randtimeszustak = random.randint(1, 5)
            self.move = True
        self.text = "Seconds: " + str(self.seconds_food)
        self.textScore = "Score: " + str(self.score)
        self.screen.blit(self.myfont.render(self.text, True, (255, 0, 0)), (32, 48))
        self.screen.blit(self.myfont.render(self.textScore, True, (255, 0, 0)), (400, 48))
        self.player.draw()
        if self.food:
            self.food.draw()
        if self.szustak:
            self.szustak.draw()

    def detectCollision(self, object):
        if self.player.pos[0]+ self.player.size[0] >= object.pos[0] >= self.player.pos[0] and self.player.pos[1]+self.player.size[1] >= object.pos[1] >= self.player.pos[1]:
            return True
        elif self.player.pos[0] + self.player.size[0] >= object.pos[0]+ object.size[0] >= self.player.pos[0] and self.player.pos[
            1] + self.player.size[1] >= object.pos[1] >= self.player.pos[1]:
            return True
        elif self.player.pos[0] + self.player.size[0] >= object.pos[0] >= self.player.pos[
            0] and self.player.pos[
                       1] + self.player.size[1] >= object.pos[1]+object.size[1] >= self.player.pos[1]:
            return True
        elif self.player.pos[0] + self.player.size[0] >= object.pos[0]+object.size[0] >= self.player.pos[
            0] and self.player.pos[
                       1] + self.player.size[1] >= object.pos[1] + object.size[1] >= self.player.pos[1]:
            return True
        else:
            return False

    def paused(self):
        self.screen.fill((0, 0, 0))
        largeText = pygame.font.SysFont("comicsansms", 115)
        self.screen.blit(largeText.render("Paused", True, (255, 255, 255)), (500, 200))
        pygame.display.update()
        while self.pause:
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.pause = False

                elif event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)


    def gameOver(self):
        self.screen.fill((0, 0, 0))
        self.endText = "GAME OVER"
        self.screen.blit(self.myfont.render(self.endText, True, (255, 255, 255)), (550, 300))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

#if __name__ == "__main__":
    # Game()
