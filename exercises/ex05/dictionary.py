"""Dictionary EX05."""

__author__ = "730704805"


def invert(dic: dict[str, str]) -> dict[str, str]:
    """Invert."""
    dictout: dict[str, str] = {}
    for key in dic:
        if dic[key] in dictout:
            raise KeyError("Duplicate Key!")
        dictout[dic[key]] = key
    return dictout


def favorite_color(dic: dict[str, str]) -> str:
    """Favorite color."""
    colors: dict[str, int] = {}
    for key in dic:
        if dic[key] in colors:
            colors[dic[key]] += 1
        else:
            colors[dic[key]] = 1
    high = 0
    fav = ""
    for cols in colors:
        if colors[cols] > high:
            high = colors[cols]
            fav = cols
    return fav


def count(ls: list[str]) -> dict[str, int]:
    """Count."""
    dictout: dict[str, int] = {}
    for i in ls:
        if i in dictout:
            dictout[i] += 1
        else:
            dictout[i] = 1
    return dictout


def alphabetizer(ls: list[str]) -> dict[str, list[str]]:
    """Alphabetizer."""
    dictout: dict[str, list[str]] = {}
    for i in ls:
        if i.lower()[0] in dictout:
            dictout[i.lower()[0]].append(i)
        else:
            dictout[i.lower()[0]] = [i]
    return dictout


def update_attendance(dic: dict[str, list[str]], day: str, student: str) -> None:
    """Update attendance."""
    if day in dic:
        if not (student in dic[day]):
            dic[day].append(student)
    else:
        dic[day] = [student]
