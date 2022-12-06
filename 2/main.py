with open("2/input.txt", "r") as file:
    lines = list(map(lambda s: s.strip(), file.readlines()))

POINTS = {"X": 1, "Y": 2, "Z": 3}
WILL_WIN = {"A Y": True, "A Z": False, "B X": False, "B Z": True, "C X": True, "C Y": False}
WINS = {"X": False, "Z": True}

MOVES = {
    "False": {"A": "Z", "B": "X", "C": "Y"},
    "True": {"A": "Y", "B": "Z", "C": "X"},
    "None": {"A": "X", "B": "Y", "C": "Z"},
}


def part_1() -> int:
    total_score = 0

    for line in lines:
        win = WILL_WIN.get(line)

        if win is None:
            total_score += 3
        elif win:
            total_score += 6

        total_score += POINTS[line[2]]

    return total_score


def part_2() -> int:
    total_score = 0

    for line in lines:
        should_win = WINS.get(line[2])

        if should_win is None:
            total_score += 3
        elif should_win:
            total_score += 6

        total_score += POINTS[MOVES[str(should_win)][line[0]]]

    return total_score


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
