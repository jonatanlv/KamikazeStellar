from typing import Dict, List

from pygame.math import Vector2
from pygame.sprite import Sprite, Group

from utils import limit

_RADIO_ACCION = 100
_MAX_ACC = 0.6


def separation(me: Sprite, neigbours: List[Sprite]) -> Vector2:
    center = me.pos
    res = Vector2()
    for n in neigbours:
        sep = center - n.pos
        m_sep = sep.magnitude()
        res += sep / m_sep

    return res


def alignment(me: Sprite, neigbours: List[Sprite]) -> Vector2:
    if len(neigbours) == 0:
        return Vector2()

    res = Vector2()
    for n in neigbours:
        res += n.vel

    return res / len(neigbours) - me.vel


def cohesion(me: Sprite, neigbours: List[Sprite]) -> Vector2:
    if len(neigbours) == 0:
        return Vector2()

    center = me.pos
    res = Vector2()
    for n in neigbours:
        res += n.pos

    return res / len(neigbours) - center


# todo Quitar los pesos porque se está pasando la responsabilidad de los pesos al cliente
forces = [(separation, 1), (alignment, 1), (cohesion, 1)]


class FlockElement:
    _steer = {}

    def set_steer(self, steer: Dict) -> None:
        self._steer = steer

    def pop_steer(self) -> Dict:
        """Devuelve la aceleración actual y la inicializa"""
        result = self._steer
        self._steer = {}
        return result


class Flock(Group):
    """Calcula la aceleración de cada elemento y la aplica a cada uno de ellos\n
    Se presupone que cada elemento tendrá un vector pos: Vector2 y vel: Vector2, representando, respectivamente la posición y la velocidad.\n
    La aceleración es la suma de 3 componentes tal y como se pueden ver en este paper: https://www.red3d.com/cwr/boids
    """

    def update_flock(self):
        cercanias = self.cernanos()
        for s in self.sprites():
            steer = {}
            for f, weight in forces:
                new_acc = f(s, cercanias[id(s)])
                limit(new_acc, _MAX_ACC)
                steer[f.__name__] = new_acc

            s.set_steer(steer)

    def cernanos(self) -> Dict:
        """Devuelve un dict donde las claves son las id de los sprites y los valores son los sprites cercanos"""
        res = {}
        sprites_l = self.sprites()
        for i in range(len(sprites_l)):
            s_i = sprites_l[i]
            res.setdefault(id(s_i), [])
            for j in range(i + 1, len(sprites_l)):
                s_j = sprites_l[j]
                # Si están cerca...
                if s_i.pos.distance_to(s_j.pos) <= _RADIO_ACCION:
                    # ...son vecinos
                    res.get(id(s_i)).append(sprites_l[j])
                    res.get(id(s_j), []).append(sprites_l[i])

        return res
