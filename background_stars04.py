# Clase para los sprites
import pygame
from settings import *
vec = pygame.math.Vector2


class Background_stars04(pygame.sprite.Sprite):
    def __init__(self, file, player_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(file).convert()
        self.rect = self.image.get_rect()
        self.pos = vec(0, 0)
        self.player_pos = player_pos
        self.rect.topleft = self.pos




    def update(self):

        self.pos.x = self.rect.width  - (self.player_pos.x % self.rect.width)
        self.pos.y = self.rect.height - (self.player_pos.y % self.rect.height)
        self.rect.topleft = self.pos

