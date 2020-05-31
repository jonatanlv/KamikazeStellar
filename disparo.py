import pygame

from settings import YELLOW, WIDTH, HEIGHT


class Disparo(pygame.sprite.Sprite):
    _VEL = 10

    def __init__(self, pos, direccion, *groups):
        super().__init__(*groups)
        self.pos = pos
        self.dir = direccion * self._VEL / direccion.length()

        self.image = pygame.Surface((9, 9), pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (4, 4), 4)
        self.mask = pygame.sprite.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.w, self.h = self.image.get_size()

    def update(self):
        self.pos += self.dir
        if self.pos.x > WIDTH + self.w or self.pos.x < -self.w or self.pos.y < -self.h or self.pos.y > HEIGHT + self.h:
            self.kill()
            return

        self.rect.center = self.pos
