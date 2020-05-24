# Importamos librerias

import pygame
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        #inicializar ventana y juego
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(GAME_NAME)
        self.clock = pygame.time.Clock()
        self.running = True

    def new(self):
        #nuevo o reiniciar juego
        self.all_sprites = pygame.sprite.Group()
        self.player = Player()
        self.stars01 = Background_stars(pos = vec(-WIDTH, -HEIGHT), file = 'image/fig01.png', player_pos= self.player.pos)
        self.stars02 = Background_stars(pos = vec(-WIDTH, 0), file = 'image/fig02.png', player_pos= self.player.pos)
        self.stars03 = Background_stars(pos = vec(-WIDTH, HEIGHT), file = 'image/fig03.png', player_pos= self.player.pos)
        self.stars04 = Background_stars(pos = vec(0, -HEIGHT), file = 'image/fig04.png', player_pos= self.player.pos)
        self.stars05 = Background_stars(pos = vec(0, 0), file = 'image/fig05.png', player_pos= self.player.pos)
        self.stars06 = Background_stars(pos = vec(0, HEIGHT), file = 'image/fig06.png', player_pos= self.player.pos)
        self.stars07 = Background_stars(pos=vec(WIDTH, -HEIGHT), file='image/fig07.png', player_pos=self.player.pos)
        self.stars08 = Background_stars(pos=vec(WIDTH, 0), file='image/fig08.png', player_pos=self.player.pos)
        self.stars09 = Background_stars(pos=vec(WIDTH, HEIGHT), file='image/fig09.png', player_pos=self.player.pos)
        self.torreta = Torreta(self.player)
        self.all_sprites.add(self.stars01, self.stars02,
        self.stars03, self.stars04, self.stars05, self.stars06, self.stars07,
        self.stars08, self.stars09, self.player, self.torreta)


    def run(self):
        #bucle del juego
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        #actualización del bucle del juego
        self.all_sprites.update()


    def events(self):
        #eventos del bucle del juego
        for event in pygame.event.get():
            # Chequeamos si el jugador ha salido del juego
            # actualizamos la variable self.playing para salir del
            # bucle dentro de run() y la variable self.running para
            # salir del juego.
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing =False
                self.running = False

    def draw(self):
        #dibuja elementos en el bucle del juego
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # pygame.display.flip() actualiza la pantalla completa
        # existe la opción de pygame.display.update()
        # que permite actualizar una parte de la pantalla.
        pygame.display.flip()

    def show_start_screen(self):
        #pantalla de inicio juego
        pass

    def show_go_screen(self):
        #pantalla fin/continue juego
        pass


g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.run()
    g.show_go_screen()

pygame.quit()