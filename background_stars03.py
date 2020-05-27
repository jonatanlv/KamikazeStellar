# Clase para los sprites
import pygame
from settings import *
vec = pygame.math.Vector2


class Background_stars03(pygame.sprite.Sprite):
    def __init__(self, pos, file, player_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(file).convert()
        self.rect = self.image.get_rect()
        self.pos = pos
        self.player_pos = player_pos
        self.rect.topleft = self.pos




    def update(self):


        if (self.player_pos.x%(3*WIDTH)) > 2*WIDTH:
            self.pos.x = WIDTH-((self.player_pos.x%(3*WIDTH))-2*WIDTH)
            self.pos.y = - (self.player_pos.y % (HEIGHT))

        self.rect.topleft = self.pos

