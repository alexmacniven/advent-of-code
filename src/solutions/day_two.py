from math import prod
from pathlib import Path
from typing import List, TextIO


def update_position(instruction: List[str], position: List[int]) -> List[int]:
    match instruction:
        case ["forward", steps]:
            position[0] += int(steps)
        case ["down", steps]:
            position[1] += int(steps)
        case ["up", steps]:
            position[1] -= int(steps)
    return position


def calc_final_position(course: List[str]) -> List[int]:
    position: List[int] = [0, 0]
    for instruction in course:
        update_position(instruction.split(' '), position)
    return position


def multiply_position(position: List[int]) -> int:
    return prod(position)


def main(course: List[str]) -> int:
    final_position: List[int] = calc_final_position(course)
    return multiply_position(final_position)


if __name__ == "__main__":
    here: Path = Path(__file__).absolute()
    depths_resource: Path = here.parents[1].joinpath("resources", "day_two", "course.txt")
    reader: TextIO
    with depths_resource.open(mode="r", encoding="utf-8") as reader:
        read_content: List[str] = reader.read()
    course: List[str] = read_content.split("\n")
    print(main(course))
