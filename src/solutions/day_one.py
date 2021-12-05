"""src.solutions.day_one

Provides a solution to the day one puzzle.
"""
from pathlib import Path
from typing import List, TextIO


def calc_depth_increases(depths: List[int]) -> int:
    return len(
        [
            depth
            for index, depth in enumerate(depths)
            if index > 0 and depth > depths[index - 1]
        ]
    )


def load_depths(resource_path: Path) -> List[int]:
    text_reader: TextIO
    with resource_path.open(mode="r", encoding="utf-8") as text_reader:
        text_content: str = text_reader.read()
    return [int(depth) for depth in text_content.split()]


def calc_measurement_windows(depths: List[int]) -> List[int]:
    return [depth + depths[index - 1] + depths[index - 2] for index, depth in enumerate(depths) if index > 1]


def main(depths_resource_path: Path) -> int:
    depths_data: List[int] = load_depths(depths_resource_path)
    measurement_windows: List[int] = calc_measurement_windows(depths_data)
    return calc_depth_increases(measurement_windows)


if __name__ == "__main__":
    here: Path = Path(__file__).absolute()
    depths_resource: Path = here.parents[1].joinpath("resources", "day_one", "depths.txt")
    print(main(depths_resource))
