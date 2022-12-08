import math


with open("8/input.txt", "r") as file:
    lines = list(map(lambda s: s.strip(), file.readlines()))

    trees = tuple([tuple(map(int, list(row.strip()))) for row in lines])


def part_1() -> int:
    visisble_trees = 0

    for i, row in enumerate(trees):
        for j, _ in enumerate(row):
            tree = trees[i][j]

            directions = [
                tuple(reversed([tree > row[j] for row in trees[:i]])),
                tuple(reversed([tree > column for column in trees[i][:j]])),
                tuple([tree > column for column in trees[i][j + 1 :]]),
                tuple([tree > row[j] for row in trees[i + 1 :]]),
            ]

            if any((all(direction) for direction in directions)):
                visisble_trees += 1

    return visisble_trees


def part_2() -> int:
    scores = []

    for i, row in enumerate(trees):
        for j, _ in enumerate(row):
            tree = trees[i][j]

            directions = [
                tuple(reversed([tree > row[j] for row in trees[:i]])),
                tuple(reversed([tree > column for column in trees[i][:j]])),
                tuple([tree > column for column in trees[i][j + 1 :]]),
                tuple([tree > row[j] for row in trees[i + 1 :]]),
            ]

            scores.append(
                math.prod(
                    [direction.index(False) + 1 if (False in direction) else len(direction) for direction in directions]
                )
            )

    return max(*scores)


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
