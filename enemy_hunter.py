# Clase para los sprites
import pygame
import random
from settings import *
vec = pygame.math.Vector2


class Hunter(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SIZE_ENEMY, SIZE_ENEMY))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        random_position = random.uniform(0, WIDTH)
        self.rect.center = (random_position, 0)
        self.pos = vec(random_position, 0)
        self.vel = vec(0, 0)
        self.coef_vel = random.uniform(VEL_MIN_HUNTER, VEL_MAX_HUNTER)

    def update(self, player_position):
        direction2player = player_position - self.pos
        self.vel = direction2player/direction2player.magnitude()
        self.pos +=  self.coef_vel * self.vel


        self.rect.center = self.pos