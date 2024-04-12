"""Functions that implement sorting algorithms."""

__author__ = "730704805"


def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm. Insert into an already sorted list."""
    for i in range(1, len(x)):
        for b in range(i, 0, -1):
            if x[b] < x[b - 1]:
                c: int = x[b]
                x.pop(b)
                x.insert(b - 1, c)


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. Repeatedly find the minimum and swap it."""
    for i in range(len(x)):
        minb: int = i
        for b in range(i, len(x)):
            if x[b] < x[minb]:
                minb = b
        x.insert(i, x[minb])
        x.pop(minb + 1)