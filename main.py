# Importamos librerias
from enemy_point import Pointer
from flock import Flock
from sprites import *


class Game:
    def __init__(self):
        # inicializar ventana y juego
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(GAME_NAME)
        self.clock = pygame.time.Clock()
        self.running = True

    def new(self):
        # nuevo o reiniciar juego
        self.all_sprites = pygame.sprite.Group()
        self.flock = Flock()
        self.player = Player()
        # self.hunter = Hunter()
        # self.chaser = Chaser()
        for i in range(10):
            Pointer(self.player, self.flock, self.all_sprites)
        self.all_sprites.add(self.player)

    def run(self):
        # bucle del juego
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # actualización del bucle del juego
        # self.player.pos.x, self.player.pos.y
        # self.hunter.update(player_position=self.player.pos)
        # self.chaser.update(player_position=self.player.pos, hunter_position=self.hunter.pos)
        # self.player.update()
        self.flock.update_flock()
        self.all_sprites.update()

    def events(self):
        # eventos del bucle del juego
        for event in pygame.event.get():
            # Chequeamos si el jugador ha salido del juego
            # actualizamos la variable self.playing para salir del
            # bucle dentro de run() y la variable self.running para
            # salir del juego.
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # dibuja elementos en el bucle del juego
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # pygame.display.flip() actualiza la pantalla completa
        # existe la opción de pygame.display.update()
        # que permite actualizar una parte de la pantalla.
        pygame.display.flip()

    def show_start_screen(self):
        # pantalla de inicio juego
        pass

    def show_go_screen(self):
        # pantalla fin/continue juego
        pass


g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.run()
    g.show_go_screen()

pygame.quit()
