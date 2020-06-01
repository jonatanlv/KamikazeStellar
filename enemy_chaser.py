# Clase para los sprites
import random

import pygame

from settings import *

vec = pygame.math.Vector2


class Chaser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((SIZE_CHASER, SIZE_CHASER))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        random_position = random.uniform(0, WIDTH)
        self.rect.center = (random_position, 0)
        self.pos = vec(random_position, 0)
        self.vel = vec(0, 0)
        self.coef_vel = random.uniform(VEL_MIN_CHASER, VEL_MAX_CHASER)

    def update(self, player_position, hunter_position):
        direction2player = player_position - self.pos
        direction2hunter = self.pos - hunter_position
        vel2player = direction2player/direction2player.magnitude()
        vel2hunter = direction2hunter/direction2hunter.magnitude()
        self.vel = ALPHA_CHASER * vel2player + (1-ALPHA_CHASER)* vel2hunter
        self.pos += self.coef_vel * self.vel



        self.rect.center = self.pos