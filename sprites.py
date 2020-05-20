# Clase para los sprites
import pygame
from pygame.math import Vector2 as Vec

from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 40))
        self.image.fill(pygame.color.THECOLORS["darkslategray4"])
        self.rect = self.image.get_rect()
        self.rect.center = Vec(WIDTH / 2, 2 * HEIGHT / 3)
        self.pos = self.rect.center
        self.vel = Vec(0, 0)

    def update(self):
        keys = pygame.key.get_pressed()
        acc = Vec(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT],
                  keys[pygame.K_DOWN] - keys[pygame.K_UP]) * ACCELERATION
        if acc.length() > ACCELERATION:
            acc *= ACCELERATION / acc.length()

        self.vel += acc
        if self.vel.length() > VELMAX:
            self.vel *= VELMAX / self.vel.length()
            acc = Vec(0, 0)

        self.rect.center += self.vel + 0.5 * acc

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH - 1
            self.vel.x = -self.vel.x / 2
        elif self.rect.left < 0:
            self.rect.left = 1
            self.vel.x = -self.vel.x / 2

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT - 1
            self.vel.y = -self.vel.y / 2
        elif self.rect.top < 0:
            self.rect.top = 1
            self.vel.y = -self.vel.y / 2

        self.pos = self.rect.center
