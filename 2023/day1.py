"""
Advent of Code 2023 - DAY 1
Paul Lee
"""

import re
from pathlib import Path

DAY1_PATH: Path = Path(__file__).parent / "bin" / "day1.txt"
PART_TWO_ENABLED: bool = False
WORD_TO_NUMBER: dict[str, int] = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_int(number: str) -> int:
    """
    returns the int value from a string

    checks for whether the number is a word (ex: "five")
    """
    if number in WORD_TO_NUMBER:
        return WORD_TO_NUMBER[number]
    return int(number)


if __name__ == "__main__":
    calibration_value_total: int = 0

    pattern: str = r"[0-9]"
    if PART_TWO_ENABLED:
        # to get overlapping matches, we do a lookahead assertion
        pattern: str = r"(?=(one|two|three|four|five|six|seven|eight|nine|[0-9]))"

    with open(DAY1_PATH, mode="r", encoding="utf-8") as day1:
        for line in day1.readlines():
            numbers: list[str] = re.findall(pattern, line)
            calibration_value_total += (get_int(numbers[0]) * 10) + get_int(numbers[-1])

    print(
        f"calibration_value_total={calibration_value_total}",
        f"with PART_TWO_ENABLED={PART_TWO_ENABLED}",
    )
