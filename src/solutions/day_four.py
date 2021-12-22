import pathlib

from typing import List, Iterable, Sequence


Path = pathlib.Path


def _check_winning_iterable(collection_: Iterable) -> bool:
    return any([all(number == '*' for number in sequence) for sequence in collection_])


def _load_draws(resource_: Path) -> List[int]:
    with resource_.open(encoding="utf-8") as reader:
        raw: str = reader.read()
    return [int(number) for number in raw.split(",")]


def _load_boards(resource_: Path) -> List[List[List[int]]]:
    _boards: List[List[List[int]]] = []
    raw: str = resource_.read_text("utf-8")
    raw_boards: List[str] = raw.split("\n\n")
    for board in raw_boards:
        rows: List[str] = board.split('\n')
        formatted_board: List[List[int]] = [[int(number) for number in row.split(" ") if number != ""] for row in rows]
        _boards.append(formatted_board)
    return _boards


class Board:
    rows: List[List[int]]
    blotted: int
    last_blotted: int
    complete: bool

    def __init__(self, rows_: List[List[int]]):
        self.rows = rows_
        self.blotted = 0
        self.last_blotted = -1
        self.complete = False

    @property
    def columns(self) -> List[List[int]]:
        return [[a[b] for a in self.rows] for b in range(len(self.rows[0]))]

    def blot(self, number_: int) -> bool:
        has_blotted: bool = False
        row: List[int | str]
        for row in self.rows:
            if number_ in row:
                row[row.index(number_)] = '*'
                self.blotted += 1
                self.last_blotted = number_
                has_blotted = True
        return has_blotted

    def check_winning_rows(self) -> bool:
        return _check_winning_iterable(self.rows)

    def check_winning_columns(self) -> bool:
        return _check_winning_iterable(self.columns)

    def calculate_score(self) -> int:
        sum_remaining_numbers: int = sum([int(n) for row in self.rows for n in row if n != "*"])
        score: int = sum_remaining_numbers * self.last_blotted
        return score


def part_one(drawn_numbers_: List[int], boards_: List[List[List[int]]]) -> int:
    board_list: Sequence[Board] = [Board(rows) for rows in boards_]
    for number in drawn_numbers_:
        for board in board_list:
            board.blot(number)
            if board.blotted >= 5 and any((board.check_winning_rows(), board.check_winning_columns())):
                return board.calculate_score()


def part_two(drawn_numbers_: List[int], boards_: List[List[List[int]]]) -> int:
    board_list: Sequence[Board] = [Board(rows) for rows in boards_]
    for number in drawn_numbers_:
        for board in board_list:
            if not board.complete:
                board.blot(number)
                if board.blotted >= 5 and any((board.check_winning_rows(), board.check_winning_columns())):
                    board.complete = True
                    board_score: int = board.calculate_score()
        if all([board.complete for board in board_list]):
            return board_score


if __name__ == "__main__":
    here: Path = Path(__file__).absolute()
    resource: Path = here.parents[1].joinpath("resources", "day_four")
    draws: List[int] = _load_draws(resource.joinpath("draws.txt"))
    boards: List[List[List[int]]] = _load_boards(resource.joinpath("boards.txt"))
    print(f"Part One: {part_one(draws, boards)}")
    print(f"Part Two: {part_two(draws, boards)}")