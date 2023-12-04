"""
Advent of Code 2023 - DAY 2
Paul Lee
"""

from pathlib import Path

DAY2_PATH: Path = Path(__file__).parent / "bin" / "day2.txt"
MAX_RED: int = 12
MAX_GREEN: int = 13
MAX_BLUE: int = 14

if __name__ == "__main__":
    valid_game_id_sum: int = 0
    power_set_sum: int = 0

    with open(DAY2_PATH, mode="r", encoding="utf-8") as day2:
        for game in day2.readlines():
            split_by_game_id: list[str] = game.replace(";", ",").split(":")
            split_by_colors: list[str] = [
                color.strip() for color in split_by_game_id[1].split(",")
            ]

            max_red: int = 0
            max_green: int = 0
            max_blue: int = 0
            for color in split_by_colors:
                if "red" in color:
                    max_red: int = max(int(color[:-3]), max_red)
                elif "green" in color:
                    max_green: int = max(int(color[:-5]), max_green)
                elif "blue" in color:
                    max_blue: int = max(int(color[:-4]), max_blue)

            if max_red <= MAX_RED and max_green <= MAX_GREEN and max_blue <= MAX_BLUE:
                # PART ONE
                valid_game_id_sum += int(split_by_game_id[0][4:])

            # PART TWO
            power_set_sum += max_red * max_green * max_blue

    print(
        f"part one -> valid_game_id_sum={valid_game_id_sum}\n",
        f"part two -> power_set_sum={power_set_sum}",
    )
