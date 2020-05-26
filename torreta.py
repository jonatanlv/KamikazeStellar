import math
from typing import Tuple

import pygame
from pygame.math import Vector2 as Vec

from settings import HEIGHT, WIDTH


class Torreta(pygame.sprite.Sprite):
    def __init__(self, player, anchor=None):
        super().__init__()
        self.player = player
        self.original_image = pygame.image.load("imagenes/torreta.png")
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = pygame.mouse.get_pos()
        self.anchor = anchor

        # Variables necesarias para la rotación
        self.pivot = Vec(15, 22)  # punto sobre el que gira la torreta relativo al topleft de la propia imagen
        self.w, self.h = self.original_image.get_size()

    def update(self):
        pos = self.player.anchors.get(self.anchor) + self.player.pos
        # aim_pos = pygame.mouse.get_pos()
        aim_pos = (WIDTH / 2, HEIGHT / 2)
        # Calcular el ángulo de giro
        angle = -Vec(0, -1).angle_to(Vec(aim_pos[0] - pos[0], aim_pos[1] - pos[1]))

        # Hacer la rotación de la torreta
        tr = rotation_traslation(*self.original_image.get_size(), self.pivot, angle)
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(topleft=(pos[0] + tr[0], pos[1] + tr[1]))


def rotation_traslation(w: int, h: int, pivot: pygame.math.Vector2, angle: float) -> Tuple[int, int]:
    """Devuelve la traslación necesaria a aplicar a un sprite que se ha rotado alrededor del pivot en un ángulo angle\n
    Es decir, devuelve el vector que va desde el pivot en la figura rotada hasta la esquina superior izquierda del AABB\n
    w: ancho original de la imagen (antes de rotar)\n
    h: alto original de la imagen (antes de rotar)\n
    pivot: Punto sobre el que se rotará la imagen\n
    angle: ángulo de rotación en grados
    """
    sin_a, cos_a = math.sin(math.radians(angle)), math.cos(math.radians(angle))
    min_x = min([0, sin_a * h, cos_a * w, sin_a * h + cos_a * w])
    min_y = max([0, sin_a * w, -cos_a * h, sin_a * w - cos_a * h])

    # calculate the translation of the pivot
    n_pivot = Vec(pivot.x, -pivot.y)
    pivot_rotate = n_pivot.rotate(angle)
    pivot_move = pivot_rotate - n_pivot

    # calculate the upper left origin of the rotated image
    return -pivot[0] + min_x - pivot_move[0], -pivot[1] - min_y + pivot_move[1]
