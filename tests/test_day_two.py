from typing import List

import pytest

from src.solutions.day_two import calc_final_position, multiply_position, main


@pytest.fixture
def course() -> List[str]:
    return [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2",
    ]


def test_calc_final_position(course: List[str]) -> None:
    expecting: List[int] = [15, 10]
    actual: List[int] = calc_final_position(course)
    assert actual == expecting


def test_multiply_position() -> None:
    expecting: int = 150
    actual: int = multiply_position([15, 10])
    assert actual == expecting


def test_main(course: List[str]) -> None:
    expecting: int = 150
    actual: int = main(course)
    assert actual == expecting
