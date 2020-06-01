# Clase para los sprites
import pygame

from settings import *

vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(SIZE_PLAYER)
        self.image.fill(GRAY2)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, 2*HEIGHT/3)
        self.pos = vec(WIDTH/2, 2*HEIGHT/3)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):
        self.acc = vec(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -ACCELERATION_PLAYER
        if keys[pygame.K_RIGHT]:
            self.acc.x = ACCELERATION_PLAYER
        if keys[pygame.K_DOWN]:
            self.acc.y = ACCELERATION_PLAYER
        if keys[pygame.K_UP]:
            self.acc.y = -ACCELERATION_PLAYER
        if keys[pygame.K_l]:
            self.vel.update((0, 0))

        self.cond1 = (self.vel.x < - VEL_MAX_PLAYER) & (self.acc.x < 0)
        self.cond2 = (self.vel.x > VEL_MAX_PLAYER) & (self.acc.x > 0)
        self.cond3 = (self.vel.y < - VEL_MAX_PLAYER) & (self.acc.y < 0)
        self.cond4 = (self.vel.y > VEL_MAX_PLAYER) & (self.acc.y > 0)
        if (self.cond1 or self.cond2 or self.cond3 or self.cond4):
            self.acc = vec(0, 0)
            self.vel += self.acc
            self.pos += self.vel + 0.5 * self.acc
        else:
             self.vel += self.acc
             self.pos += self.vel + 0.5 * self.acc


        if self.pos.x > WIDTH-SIZE_PLAYER[0]/2:
            self.pos.x = WIDTH-SIZE_PLAYER[0]/2
            self.vel = vec(0, 0)

        if self.pos.x < SIZE_PLAYER[0]/2:
            self.pos.x = SIZE_PLAYER[0]/2
            self.vel = vec(0, 0)

        if self.pos.y > HEIGHT-SIZE_PLAYER[1]/2:
            self.pos.y = HEIGHT-SIZE_PLAYER[1]/2
            self.vel = vec(0, 0)

        if self.pos.y < SIZE_PLAYER[1]/2:
            self.pos.y = SIZE_PLAYER[1]/2
            self.vel = vec(0, 0)


        self.rect.center = self.pos