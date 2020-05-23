# Clase para los sprites
import pygame
from settings import *
vec = pygame.math.Vector2


class Background_stars(pygame.sprite.Sprite):
    def __init__(self, pos, file, player_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(file).convert()
        self.rect = self.image.get_rect()
        self.pos = pos
        self.player_pos = player_pos
        self.rect.topleft = self.pos
        self.pos += self.player_pos
        self.pos_rel = vec(0, 0)


    def update(self):
        self.pos_rel = self.pos - self.player_pos

        #if self.pos_rel.x < -WIDTH:
        #    self.pos_rel.x = WIDTH- self.player_pos.x
        #if self.pos_rel.x > WIDTH:
        #    self.pos_rel.x = -WIDTH - self.player_pos.x

        self.rect.topleft = self.pos_rel
