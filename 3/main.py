import string


with open("3/input.txt", "r") as file:
    lines = list(map(lambda s: s.strip(), file.readlines()))


def part_1() -> int:
    total_priority = 0

    for line in lines:
        compartments = [line[:len(line) // 2], line[len(line) // 2:]]

        for item in compartments[0]:
            if compartments[1].find(item) != 1:
                total_priority += string.ascii_letters.index(item) + 1

    return total_priority

def part_2() -> int:
    total_priority = 0

    return total_priority


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
