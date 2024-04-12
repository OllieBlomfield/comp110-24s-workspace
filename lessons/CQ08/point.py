"""Point class challenge question."""
from __future__ import annotations

__author__ = "730704805"


class Point:
    """Point class."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Mutates self."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Creates new point."""
        return Point(self.x * factor, self.y * factor)