"""Utils."""

__author__ = "730704805"


def all(l1: list[int], n: int) -> bool:
    """Returns True if all values in list l are equal to n."""
    if len(l1) == 0:
        return False
    for i in range(len(l1)):
        if l1[i] != n:
            return False
    return True


def max(l1: list[int]) -> int:
    """Returns the maximum value in the list l."""
    if len(l1) == 0:
        raise ValueError("max() arg is an empty List")
    current_max = l1[0]
    for i in range(len(l1)):
        if l1[i] > current_max:
            current_max = l1[i]
    return current_max


def is_equal(l1: list[int], l2: list[int]) -> bool:
    """Returns True if all values in the function are equal. Deep equality."""
    if len(l1) != len(l2):
        return False
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False
    return True


def extend(l1: list[int], l2: list[int]) -> None:
    """Adds the values of l2 to the list l1."""
    for i in range(len(l2)):
        l1.append(l2[i])
    