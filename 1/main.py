with open("1/input.txt", "r") as file:
    lines = list(map(lambda s: s.strip(), file.readlines()))


def get_inventories():
    inventories = [0]

    for line in lines:
        if not line:
            inventories.append(0)
        else:
            inventories[-1] += int(line)

    return inventories


def part_1() -> int:
    return max(*get_inventories())


def part_2() -> int:
    return sum(sorted(get_inventories(), reverse=True)[:3])


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
