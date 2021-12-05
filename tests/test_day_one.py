from pathlib import Path
from typing import List, TextIO

import pytest

from src.solutions.day_one import calc_depth_increases, load_depths, calc_measurement_windows, main


@pytest.fixture
def depths() -> List[int]:
    return [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263,
    ]


@pytest.fixture
def depths_resource_path(depths: List[int], tmp_path: Path) -> Path:
    depths_resource_path_: Path = tmp_path.joinpath("depths.txt")
    writer: TextIO
    with depths_resource_path_.open("w", encoding="utf-8") as writer:
        writer.write("\n".join([str(depth) for depth in depths]))
    return depths_resource_path_


def test_calc_depth_increases(depths: List[int]):
    expecting: int = 7
    actual: int = calc_depth_increases(depths)
    assert actual == expecting


def test_load_depths(tmp_path: Path, depths: List[int]) -> None:
    depths_resource: Path = tmp_path.joinpath("depths.txt")
    text_writer: TextIO
    with depths_resource.open(mode="w", encoding="utf-8") as text_writer:
        text_writer.write("199\n200\n208\n210\n200\n207\n240\n269\n260\n263")
    expecting: List[int] = depths
    actual: List[int] = load_depths(depths_resource)
    assert actual == expecting


def test_main(depths_resource_path: Path) -> None:
    expecting: int = 5
    actual: int = main(depths_resource_path)
    assert actual == expecting


def test_calc_measurement_windows(depths: List[int]) -> None:
    expecting: List[int] = [
        607,
        618,
        618,
        617,
        647,
        716,
        769,
        792,
    ]
    actual: List[int] = calc_measurement_windows(depths)
    assert actual == expecting
