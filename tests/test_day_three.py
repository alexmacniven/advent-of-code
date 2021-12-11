from typing import Sequence

import pytest

from src.solutions.day_three import format_column_binary, eval_most_common_bit, flip_bits, convert_to_decimal, \
    calc_power_consumption, eval_oxygen_generator_rating, eval_co2_scrubber_rating


@pytest.fixture
def diagnostics() -> Sequence[str]:
    return [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]


@pytest.fixture
def column_binary() -> Sequence[Sequence[str]]:
    return [
        ['0', '1', '1', '1', '1', '0', '0', '1', '1', '1', '0', '0'],
        ['0', '1', '0', '0', '0', '1', '0', '1', '0', '1', '0', '1'],
        ['1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0'],
        ['0', '1', '1', '1', '0', '1', '1', '0', '0', '0', '1', '1'],
        ['0', '0', '0', '1', '1', '1', '1', '0', '0', '1', '0', '0']
    ]


@pytest.fixture
def gamma() -> str:
    return "10110"


@pytest.fixture
def epsilon() -> str:
    return "01001"


def test_format_column_binary(diagnostics: Sequence[str], column_binary: Sequence[str]) -> None:
    actual: Sequence[Sequence[str]] = format_column_binary(diagnostics)
    assert actual == column_binary


def test_eval_most_common_bit(column_binary: Sequence[str], gamma: str) -> None:
    actual: Sequence[str] = eval_most_common_bit(column_binary)
    assert actual == gamma


def test_flip_bits(gamma: str, epsilon: str) -> None:
    actual: str = flip_bits(gamma)
    assert actual == epsilon


@pytest.mark.parametrize("binary,decimal", [("10110", 22), ("01001", 9)])
def test_convert_to_decimal(binary: str, decimal: int) -> None:
    actual: int = convert_to_decimal(binary)
    assert actual == decimal


def test_calc_power_consumption(diagnostics: Sequence[str]) -> None:
    expecting: int = 198
    actual: int = calc_power_consumption(diagnostics)
    assert actual == expecting


def test_eval_oxygen_generator_rating(diagnostics: Sequence[str]) -> None:
    expecting: str = "10111"
    actual: str = eval_oxygen_generator_rating(diagnostics)
    assert actual == expecting


def test_eval_co2_scrubber_rating(diagnostics: Sequence[str]) -> None:
    expecting: str = "01010"
    actual: str = eval_co2_scrubber_rating(diagnostics)
    assert actual == expecting



