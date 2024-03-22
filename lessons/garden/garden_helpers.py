"""Some functions for my garden plan!"""

__author__ = "730704805"


def add_by_kind(garden_dict: dict[str, list[str]], type: str, plant: str) -> None:
    """Adds a new plant to the garden dictionary based on plant type."""
    if type in garden_dict:
        garden_dict[type].append(plant)
    else:
        garden_dict[type] = []
        garden_dict[type].append(plant)


def add_by_date(garden_dict: dict[str, list[str]], date: str, plant: str) -> None:
    """Adds a new plant to the garden dictionary based on date."""
    if date in garden_dict:
        garden_dict[date].append(plant)
    else:
        garden_dict[date] = []
        garden_dict[date].append(plant)


def lookup_by_kind_and_date(garden_dict_kind: dict[str, list[str]], garden_dict_date: dict[str, list[str]], kind: str, date: str) -> str:
    """Searches through 2 dictionaries to find plants that are both in that date and type."""
    valid_plants: list[str] = []
    if kind in garden_dict_kind and date in garden_dict_date:
        for pl1 in garden_dict_date[date]:
            for pl2 in garden_dict_kind[kind]:
                if pl1 == pl2:
                    valid_plants.append(pl1)
     
    if len(valid_plants) > 0:
        return f"{kind}s to plant in {date}: {valid_plants}"
    else:
        return f"No {kind}s to plant in {date}."
                     