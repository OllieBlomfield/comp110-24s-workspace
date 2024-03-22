"""Summing the elements of a list using different loops."""

__author__ = "730704805"


def w_sum(vals: list[float]) -> float:
    """Sum of list with while loop."""
    counter: int = 0
    sum: float = 0.0
    if len(vals) == 0:
        return 0.0
    while counter < len(vals):
        sum += vals[counter]
        counter += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Sum of list with for loop (i in vals)."""
    sum: float = 0.0
    if len(vals) == 0:
        return 0.0
    for i in vals:
        sum += i
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Some of list with for loop range."""
    sum: float = 0.0
    if len(vals) == 0:
        return 0.0
    for i in range(len(vals)):
        sum += vals[i]
    return sum
