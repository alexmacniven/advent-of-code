from copy import copy
from pathlib import Path
from typing import Sequence, TextIO, List


def format_column_binary(diagnostics: Sequence[str]) -> Sequence[Sequence[str]]:
    return [[binary[item] for binary in diagnostics] for item in range(len(diagnostics[0]))]


def eval_most_common_bit(column_binary: Sequence[Sequence[str]]) -> str:
    common_bits: Sequence[str] = ["1" if column.count("1") >= column.count("0") else "0" for column in column_binary]
    return "".join(common_bits)


def flip_bits(binary: str) -> str:
    flipped_bits: Sequence[str] = ["1" if bit == "0" else "0" for bit in binary]
    return "".join(flipped_bits)


def convert_to_decimal(binary: str) -> int:
    return int(binary, 2)


def calc_power_consumption(diagnostics: Sequence[str]) -> int:
    column_binary: Sequence[Sequence[str]] = format_column_binary(diagnostics)
    gamma_binary: str = eval_most_common_bit(column_binary)
    epsilon_binary: str = flip_bits(gamma_binary)
    gamma_int: int = convert_to_decimal(gamma_binary)
    epsilon_int: int = convert_to_decimal(epsilon_binary)
    return gamma_int * epsilon_int


def filter_on_common(diagnostics: Sequence[str], filter_index: int, filter_least_common: bool) -> str:
    column_binary: Sequence[Sequence[str]] = format_column_binary(diagnostics)
    common_bits_binary_: str = eval_most_common_bit(column_binary)
    common_bits_binary: str = flip_bits(common_bits_binary_) if filter_least_common else common_bits_binary_
    filtered_diagnostics: Sequence[str] = [diag for diag in diagnostics if diag[filter_index] == common_bits_binary[filter_index]]
    if len(filtered_diagnostics) == 1:
        return filtered_diagnostics[0]
    else:
        return filter_on_common(filtered_diagnostics, filter_index + 1, filter_least_common)


def eval_oxygen_generator_rating(diagnostics: Sequence[str]) -> str:
    return filter_on_common(diagnostics, 0, False)


def eval_co2_scrubber_rating(diagnostics: Sequence[str]) -> str:
    return filter_on_common(diagnostics, 0, True)


def calc_life_support_rating(diagnostics: Sequence[str]) -> int:
    oxygen_binary: str = eval_oxygen_generator_rating(diagnostics)
    co2_binary: str = eval_co2_scrubber_rating(diagnostics)
    oxygen_rating: int = convert_to_decimal(oxygen_binary)
    co2_rating: int = convert_to_decimal(co2_binary)
    return oxygen_rating * co2_rating


if __name__ == "__main__":
    here: Path = Path(__file__).absolute()
    resource: Path = here.parents[1].joinpath("resources", "day_three", "diagnostics.txt")
    reader: TextIO
    with resource.open(mode="r", encoding="utf-8") as reader:
        read_content: str = reader.read()
    diagnostics: Sequence[str] = read_content.split("\n")
    print("Power consumption:", end=" ")
    print(calc_power_consumption(diagnostics))
    print("Life support rating:", end=" ")
    print(calc_life_support_rating(diagnostics))
