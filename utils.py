from numbers import Number

from pygame.math import Vector2


def limit(v: Vector2, max_m: float) -> None:
    """Limita la magnitud del vector v "in place" a max_m"""
    m_2 = v.magnitude_squared()
    if m_2 > max_m ** 2:
        v.scale_to_length(max_m)


def in_range(a: Number, min_a: Number, max_a: Number):
    """Devuelve un valor de a que esté en el intervalo [min_a, max_a]"""
    if min_a > max_a:
        raise AttributeError("min_a tiene que ser menor que max_a ({} > {})".format(min_a, max_a))
    return min(max(min_a, a), max_a)
