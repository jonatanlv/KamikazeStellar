# Importamos librerias
from pygame.sprite import collide_mask

from settings import *
from sprites import *
from torreta import *


class Game:
    def __init__(self):
        # inicializar ventana y juego
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(NAME)
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.running = True
        self.playing = True
        self.collision = None

    def new(self):
        self.player = Player()
        tr1 = Torreta(self.player, "topleft")
        tr2 = Torreta(self.player, "topright")
        tr3 = Torreta(self.player, "bottomleft")
        tr4 = Torreta(self.player, "bottomright")
        self.enemy = Enemy()
        self.all_sprites.add(self.player, self.enemy, tr1, tr2, tr3, tr4)

    def run(self):
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # actualización del bucle del juego
        self.all_sprites.update()

        # Calcular colisiones
        self.collision = collide_mask(self.player, self.enemy)

    def events(self):
        # eventos del bucle del juego
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def draw(self):
        # dibuja elementos en el bucle del juego
        self.screen.fill(self.collision is None and BLACK or RED)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()


g = Game()
while g.running:
    g.new()
    g.run()

pygame.quit()
