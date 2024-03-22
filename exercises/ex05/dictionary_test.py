"""Test functions for dictionary.py."""

__author__ = "730704805"

from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest


def test_invert_KeyError():
    """Tests for a Key Error when there is a duplicate in the values."""
    with pytest.raises(KeyError):
        my_dictionary = {'alyssa': 'byrnes', 'adam': 'byrnes'}
        invert(my_dictionary)


def test_invert_empty() -> None:
    """Tests the invert function when there is no keys or values in the dictionary."""
    assert invert({}) == {}


def test_invert_case1() -> None:
    """Tests the invert function with a standard use case."""
    assert invert({"Nancy": "Bean", "Micheal": "Lean", "Queen": "Fiend", "French": "Talent"}) == {"Bean": "Nancy", "Lean": "Micheal", "Fiend": "Queen", "Talent": "French"}


def test_invert_case2() -> None:
    """Tests the invert function with another standard use case."""
    assert invert({"Big": "Small", "md": "dm", "Help": "SOS", "Kids": "MGMT"}) == {"Small": "Big", "dm": "md", "SOS": "Help", "MGMT": "Kids"}


def test_favorite_color_empty() -> None:
    """Tests the favorite_color function when there is no keys or values in the dictionary."""
    assert favorite_color({}) == ""


def test_favorite_color_case1() -> None:
    """Tests the favorite_color function with a case where there are an equal amount of 2 colors mentioned."""
    assert favorite_color({"Izzy": "blue", "Blake": "red", "Andre": "red", "Brian": "blue"}) == "blue"


def test_favorite_color_case2() -> None:
    """Tests the favorite_color function for a standard use case."""
    assert favorite_color({"Milo": "green", "Khem": "yellow", "Kaan": "green"}) == "green"


def test_count_empty() -> None:
    """Tests the count function when there is no items in the list."""
    assert count([]) == {}


def test_count_case1() -> None:
    """Tests the count function for a case where several words appear twice."""
    assert count(["Hello", "Hi", "Wassup", "Bigman", "Hello", "Hi", "No", "No"]) == {"Hello": 2, "Hi": 2, "Wassup": 1, "Bigman": 1, "No": 2}


def test_count_case2() -> None:
    """Test the count function for a case where the word "Yo" appears very frequently."""
    assert count(["Yo", "Yo", "Yo", "Yo", "Yo", "Yo", "Yo", "Hi"]) == {"Yo": 7, "Hi": 1}

                                  
def test_alphabetizer_empty() -> None:
    """Tests the alphabetizer function when there is no items in the list."""
    assert alphabetizer([]) == {}


def test_alphabetizer_case1() -> None:
    """Tests the alphabetizer function where there are similar words with varying capitalisation."""
    assert alphabetizer(["A", "Aa", "Bean", "Zag", "chocolate", "Cake"]) == {"a": ["A", "Aa"], "b": ["Bean"], "z": ["Zag"], "c": ["chocolate", "Cake"]}


def test_alphabetizer_case2() -> None:
    """Tests the alphabetizer function for a standard use case."""
    assert alphabetizer(["cat", "apple", "boy", "angry", "bad", "car"]) == {'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}


def test_update_attendance_empty() -> None:
    """Tests the update_attendance function when there is no keys or values in the dictionary."""
    dic_test: dict = {}
    update_attendance(dic_test, "", "")
    assert dic_test == {"": [""]}


def test_update_attendance_case1() -> None:
    """Tests the update_attendance function for a standard use case."""
    dic_test: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance(dic_test, "Tuesday", "Vrinda")
    update_attendance(dic_test, "Wednesday", "Kaleb")
    assert dic_test == {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda'], 'Wednesday': ['Kaleb']}


def test_update_attendance_case2() -> None:
    """Tests the update_attendance function for a initial empty dictionary."""
    dic_test: dict = {}
    update_attendance(dic_test, "Ben", "Thursday")
    assert dic_test == {"Ben": ["Thursday"]}
