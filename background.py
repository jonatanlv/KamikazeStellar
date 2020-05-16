# Clase para los sprites
import pygame
from settings import *
vec = pygame.math.Vector2


class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('image/fondo00.png').convert()
        self.rect = self.image.get_rect()
        self.pos = vec(0, 0)
        self.acc = vec(0 ,0)
        self.vel = vec(0, 0)
        self.rect.center = self.pos


    def update(self):
        self.acc = vec(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = ACCELERATION_PLAYER
        if keys[pygame.K_RIGHT]:
            self.acc.x = -ACCELERATION_PLAYER
        if keys[pygame.K_DOWN]:
            self.acc.y = -ACCELERATION_PLAYER
        if keys[pygame.K_UP]:
            self.acc.y = ACCELERATION_PLAYER

        cond1 = (self.vel.x < - VEL_MAX_PLAYER) & (self.acc.x < 0)
        cond2 = (self.vel.x > VEL_MAX_PLAYER) & (self.acc.x > 0)
        cond3 = (self.vel.y < - VEL_MAX_PLAYER) & (self.acc.y < 0)
        cond4 = (self.vel.y > VEL_MAX_PLAYER) & (self.acc.y > 0)
        if ( cond1 or cond2 or cond3 or cond4):
             self.acc = vec(0, 0)
             self.vel += self.acc
             self.pos += self.vel + 0.5 * self.acc
        else:
             self.vel += self.acc
             self.pos += self.vel + 0.5 * self.acc


        self.rect.center = self.pos

        #if self.pos.x > WIDTH:
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
        #