# Clase para los sprites
import pygame
from settings import *
vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(GRAY2)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)


    def update(self):
        pass
        # self.acc = vec(0, 0)
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_LEFT]:
        #     self.acc.x = -ACCELERATION
        # if keys[pygame.K_RIGHT]:
        #     self.acc.x = ACCELERATION
        # if keys[pygame.K_DOWN]:
        #     self.acc.y = ACCELERATION
        # if keys[pygame.K_UP]:
        #     self.acc.y = -ACCELERATION
        #
        # self.cond1 = (self.vel.x < - VELMAX) & (self.acc.x < 0)
        # self.cond2 = (self.vel.x > VELMAX) & (self.acc.x > 0)
        # self.cond3 = (self.vel.y < - VELMAX) & (self.acc.y < 0)
        # self.cond4 = (self.vel.y > VELMAX) & (self.acc.y > 0)
        # if ( self.cond1 or self.cond2 or self.cond3 or self.cond4):
        #     self.acc = vec(0, 0)
        #     self.vel += self.acc
        #     self.pos += self.vel + 0.5 * self.acc
        # else:
        #      self.vel += self.acc
        #      self.pos += self.vel + 0.5 * self.acc
        #
        #
        # if self.pos.x > WIDTH:
        #     self.pos.x = 0
        #
        # if self.pos.x < 0:
        #     self.pos.x = WIDTH
        #
        # if self.pos.y > HEIGHT:
        #     self.pos.y = 0
        #
        # if self.pos.y < 0:
        #     self.pos.y = HEIGHT
        #
        #
        # self.rect.center = self.pos
        #