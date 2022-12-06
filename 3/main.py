import string, itertools


with open("3/input.txt", "r") as file:
    lines = list(map(lambda s: s.strip(), file.readlines()))


def part_1() -> int:
    total_priority = 0

    for line in lines:
        compartments = [line[: len(line) // 2], line[len(line) // 2 :]]

        item = [item for item in compartments[0] if item in compartments[1]][0]
        total_priority += string.ascii_letters.index(item) + 1

    return total_priority


def part_2() -> int:
    total_priority = 0

    for line_group in itertools.zip_longest(*[iter(lines)] * 3, fillvalue=""):
        total_priority += (
            string.ascii_letters.index(
                (set(line_group[0].strip()) & set(line_group[1].strip()) & set(line_group[2].strip())).pop()  # type: ignore
            )
            + 1
        )

    return total_priority


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
