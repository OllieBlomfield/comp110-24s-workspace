"""Recursive definition Challenge Question."""


def f(n: int, k: int) -> int:
    """Recursive definition of n * k."""
    if n == 0:
        return 0
    else:
        return k + f(n - 1, k)