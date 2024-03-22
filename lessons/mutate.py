"""Mutating functions."""

__author__ = "730704805"


def manual_append(unambiguousl: list[int], n: int) -> None:
    """Manual append."""
    unambiguousl.append(n)


def double(unambiguousl: list[int]) -> None:
    """Double."""
    i = 0
    while i < len(unambiguousl):
        unambiguousl[i] *= 2
        i += 1