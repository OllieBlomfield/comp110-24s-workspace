"""Test my garden functions."""

__author__ = "730704805"

from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date


def test_add_by_kind_edge() -> None:
    """Tests edge case for add_by_kind."""
    dict_test: dict[str, list[str]] = {}
    add_by_kind(dict_test, "flower", "rose")
    assert dict_test == {"flower": ["rose"]}


def test_add_by_kind_case() -> None:
    """Tests base case for add_by_kind."""
    dict_test = {"flower": ["sunflower", "rose"], "fruit": ["peach"]}
    add_by_kind(dict_test, "fruit", "apple")
    assert dict_test == {"flower": ["sunflower", "rose"], "fruit": ["peach", "apple"]}


def test_add_by_date_edge() -> None:
    """Tests edge case for add_by_date."""
    dict_test = {}
    add_by_date(dict_test, "", "")
    assert dict_test == {"": [""]}


def test_add_by_date_case() -> None:
    """Tests base case for add_by_date."""
    dict_test = {"August": ["Banana", "Cabbage"], "September": ["Carrot", "Rose"]}
    add_by_date(dict_test, "June", "Pepper")
    assert dict_test == {"August": ["Banana", "Cabbage"], "September": ["Carrot", "Rose"], "June": ["Pepper"]}


def test_lookup_by_kind_and_date_edge() -> None:
    """Tests edge case for lookup_by_kind_and_date."""
    assert lookup_by_kind_and_date({}, {"April": ["Sunflower", "Peach"]}, "flower", "June") == "No flowers to plant in June."


def test_lookup_by_kind_and_date_case() -> None:
    """Tests base case for lookup_by_kind_and_date."""
    assert lookup_by_kind_and_date({"flower": ["Lily", "Rose"], "vegetable": ["Cabbage"]}, {"January": ["Rose", "Cabbage", "Lily"]}, "flower", "January") == "flowers to plant in January: ['Rose', 'Lily']"