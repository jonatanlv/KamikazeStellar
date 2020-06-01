# Clase para los sprites
import random

import pygame
from pygame.math import Vector2

from flock import FlockElement
from settings import *
from utils import in_range

_VEL_MAX = 5
_ACC = 0.2
_DIMS = (5, 5)


class Pointer(pygame.sprite.Sprite, FlockElement):
    pos = Vector2()
    vel = Vector2()
    weights = {
        "separation": 1.5,
        "cohesion": 1.3,
        "alignment": 0
    }
    step = 0.01

    def __init__(self, player, *args):
        pygame.sprite.Sprite.__init__(self, *args)
        FlockElement.__init__(self)
        self.player = player
        self.image = pygame.Surface(_DIMS, pygame.SRCALPHA)
        # pygame.draw.polygon(self.image, BLUE,
        #                     [(_DIMS[0] // 2, 0), (0, _DIMS[1]), (_DIMS[0] // 2, 2 * _DIMS[1] // 3), _DIMS])
        # self.original_image = self.image
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        random_position = random.uniform(WIDTH // 2, WIDTH)
        self.rect.center = (random.randint(WIDTH // 4, 3 * WIDTH // 4), random.randint(HEIGHT // 4, 3 * HEIGHT // 4))
        self.pos = Vector2(self.rect.center)

    def update(self):
        keys = pygame.key.get_pressed()
        show_weights = False
        if keys[pygame.K_q] or keys[pygame.K_a]:
            show_weights = True
            self.weights["separation"] = in_range(
                self.weights["separation"] + self.step * (keys[pygame.K_q] - keys[pygame.K_a]), 0, 5)
        elif keys[pygame.K_w] or keys[pygame.K_s]:
            show_weights = True
            self.weights["cohesion"] = in_range(
                self.weights["cohesion"] + self.step * (keys[pygame.K_w] - keys[pygame.K_s]),
                0, 5)
        elif keys[pygame.K_e] or keys[pygame.K_d]:
            show_weights = True
            self.weights["alignment"] = in_range(
                self.weights["alignment"] + self.step * (keys[pygame.K_e] - keys[pygame.K_d]), 0, 5)

        if show_weights:
            for k, v in self.weights.items():
                print("{}: {}".format(k, v))

        direction2player = self.player.pos - self.pos
        # acc = _ACC * direction2player / direction2player.magnitude() + self.pop_steer()
        steer = self.pop_steer()
        acc = Vector2()
        for k, v in steer.items():
            acc += v * self.weights.get(k, 1)
        acc += _ACC * direction2player / direction2player.magnitude()
        self.vel += acc
        if self.vel.magnitude() > _VEL_MAX:
            self.vel = self.vel.normalize() * _VEL_MAX
        self.pos += self.vel
        self.rect.center = self.pos
