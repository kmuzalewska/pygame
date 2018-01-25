import pygame, sys
from panda import Panda
from bambus import Bambus
from szustak import Szustak
import random

class Game(object):
    def __init__(self):
        # Config
        self.tps_max = 100.0
        self.score=3
        # Initialization
        pygame.init()
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 50)
        self.screen = pygame.display.set_mode((1280, 720))
        self.start_ticks = pygame.time.get_ticks()
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0
        self.randtimebabmus = random.randint(1,10)
        self.randtimeszustak = random.randint(1, 15)
        self.player = Panda(self)
        self.feed = None
        self.szustak = None
        self.move=True
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            # Ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max
            self.collision()
            # Drawing
            self.screen.fill((10, 200, 0))
            self.draw()
            pygame.display.update()

    def tick(self):
        self.player.tick()
        if self.score <= 0:
            self.screen.fill((0, 0, 0))
            self.endText = "GAME OVER"
            self.screen.blit(self.myfont.render(self.endText, True, (255, 255, 255)), (550, 340))
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit(0)
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        sys.exit(0)
        if self.seconds == 0:
            self.start_ticks = pygame.time.get_ticks()
            self.score -= 1


    def draw(self):
        # Drawing
        # print self.randtimebabmus
        self.seconds = 10 - (pygame.time.get_ticks() - self.start_ticks) / 1000
        if self.seconds == self.randtimebabmus:
            self.feed = Bambus(self)
            self.randtimebabmus = random.randint(1, 10)
            self.score -= 1
        if self.seconds == self.randtimeszustak:
            self.szustak = Szustak(self)
            self.randtimeszustak = random.randint(1, 15)
            self.move = True
        self.text = "Seconds: " + str(self.seconds)
        self.textScore = "Score: " + str(self.score)
        self.screen.blit(self.myfont.render(self.text, True, (255, 0, 0)), (32, 48))
        self.screen.blit(self.myfont.render(self.textScore, True, (255, 0, 0)), (400, 48))
        self.player.draw()
        if self.feed:
            self.feed.draw()
        if self.szustak:
            self.szustak.draw()

    def collision(self):

        if self.feed:
            if self.player.pos[0]-30 <= self.feed.pos[0] <= self.player.pos[0]+30 and self.player.pos[1]-30 <= self.feed.pos[1] <= self.player.pos[1]+30:
                self.start_ticks = pygame.time.get_ticks()
                self.feed = Bambus(self)
                self.randtimebabmus = random.randint(1, 10)
                self.score+=1
        if self.szustak:
            if self.player.pos[0] - 50 <= self.szustak.pos[0] <= self.player.pos[0] + 50 and self.player.pos[1] - 150 <= \
                    self.szustak.pos[1] <= self.player.pos[1] + 150:
                self.move = False

if __name__ == "__main__":
    Game()
