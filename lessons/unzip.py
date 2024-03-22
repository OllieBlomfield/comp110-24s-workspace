"""Splitting a dictionary into two lists."""

__author__ = "730704805"


def get_keys(dic: dict[str, int]) -> list[str]:
    """Get Keys."""
    outl: list[str] = []
    for key in dic:
        outl.append(key)
    return outl


def get_values(dic: dict[str, int]) -> list[int]:
    """Get Values."""
    outl: list[int] = []
    for key in dic:
        outl.append(dic[key])
    return outl