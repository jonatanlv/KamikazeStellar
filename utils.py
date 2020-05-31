import pygame


class Timer:
    """Temporizador para el control de eventos.
    Guarda un registro de la última vez que pudo suceder e informa en cualquier momento si puede volver a suceder"""

    def __init__(self, delay: int, last=None):
        self.delay = delay
        if last is None:
            self.last = -delay
        else:
            self.last = last

    def can_happen(self, update: bool = True) -> bool:
        """Devuelve True si el evento puede suceder. En este caso"""
        now = pygame.time.get_ticks()
        if now - self.last > self.delay:
            if update:
                self.last = now
            return True

        return False
