##############################################
#### Configuración y constantes del juego ####
##############################################
import pygame


#### Constantes de ventana ####
WIDTH = 800
HEIGHT = 600
FPS = 60
NAME = "KamikazeStellar v.0.0"
#### Definición de colores ####

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GRAY1 = (213, 219, 219)
GRAY2 = (131, 145, 146)

#### Controles del juego
MOVE_UP = pygame.K_w
MOVE_DOWN = pygame.K_s
MOVE_LEFT = pygame.K_a
MOVE_RIGHT = pygame.K_d

#### Parámetros del jugador ####

ACCELERATION = 0.6
VELMAX = 15