# Clase para los sprites
import pygame
import random
from settings import *
vec = pygame.math.Vector2


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SIZE_ENEMY, SIZE_ENEMY))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        random_position = random.uniform(0, WIDTH)
        self.rect.center = (random_position, 0)
        self.pos = vec(random_position, 0)
        self.player_pos = vec(0, 0)
        self.vel = vec(0, 0)
        self.direction = vec(0, 0)
        self.coef_vel = random.uniform(VELMINENEMY, VELMAXENEMY)

    def update(self, player_position):
        self.player_pos = player_position
        self.direction = self.player_pos - self.pos
        self.vel = self.direction/self.direction.magnitude()
        self.pos +=  self.coef_vel * self.vel

        if self.pos.x > WIDTH:
            self.pos.x = 0

        if self.pos.x < 0:
            self.pos.x = WIDTH

        if self.pos.y > HEIGHT:
            self.pos.y = 0

        if self.pos.y < 0:
            self.pos.y = HEIGHT


        self.rect.center = self.pos