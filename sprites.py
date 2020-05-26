# Clase para los sprites
import pygame

from settings import RED, HEIGHT, WIDTH
from torreta import rotation_traslation

vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = pygame.image.load("imagenes/test_colision1.png").convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.angle = 0
        self.original_anchors = {
            "topleft": vec(10, 10),
            "topright": vec(90, 10),
            "bottomleft": vec(10, 90),
            "bottomright": vec(90, 90)
        }
        self.anchors = self.original_anchors.copy()
        self.pivot = vec(20, 30)
        self.pos = vec(0, 0)
        pygame.draw.circle(self.original_image, RED, (int(self.pivot.x), int(self.pivot.y)), 3, 2)

    def update(self):
        buttons = pygame.mouse.get_pressed()
        if buttons[0]:
            self.angle += 5
        if buttons[2]:
            self.angle -= 5
        self.angle %= 360
        size = self.original_image.get_size()
        tr = rotation_traslation(size[0], size[1], self.pivot, self.angle)
        for k, v in self.original_anchors.items():
            v1 = v - self.pivot
            v2 = v1.rotate(-self.angle)
            self.anchors[k] = vec(v2.x, v2.y)

        self.pos = pygame.mouse.get_pos()

        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(topleft=(self.pos[0] + tr[0], self.pos[1] + tr[1]))


class Enemy(Player):
    def update(self):
        self.angle += 0.2
        self.angle %= 360

        self.pos = (WIDTH / 2, HEIGHT / 2)
        size = self.original_image.get_size()

        tr = rotation_traslation(size[0], size[1], self.pivot, self.angle)
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(topleft=(self.pos[0] + tr[0], self.pos[1] + tr[1]))
