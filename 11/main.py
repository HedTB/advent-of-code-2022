from dataclasses import dataclass
from typing import Callable

import math


with open("11/input.txt", "r") as file:
    lines = list(map(lambda s: s.strip().splitlines(), file.read().split("\n\n")))
with open("11/test_input.txt", "r") as file:
    test_lines = list(map(lambda s: s.strip().splitlines(), file.read().split("\n\n")))


@dataclass
class Monkey:
    items: list[int]

    operation: Callable[[int], int]
    test: Callable[[int], bool]

    divisible_by: int

    if_true: int
    if_false: int

    inspected: int = 0


def get_monkeys(part: int, test: bool = False) -> list[Monkey]:
    monkeys = [
        Monkey(
            items=[int(item.removesuffix(",")) for item in monkey[1].partition(": ")[2].split()],
            operation=eval("lambda old: " + monkey[2].partition("= ")[2]),
            test=eval(f"lambda x: x % {monkey[3].partition('by ')[2]} == 0"),
            divisible_by=int(monkey[3].partition("by ")[2]),
            if_true=int(monkey[4].partition("monkey ")[2]),
            if_false=int(monkey[5].partition("monkey ")[2]),
        )
        for monkey in (test_lines if test else lines)
    ]
    lcm = 1

    for monkey in monkeys:
        lcm = math.lcm(lcm, monkey.divisible_by)

    for _ in range(20 if part == 1 else 10000):
        for monkey in monkeys:
            to_remove = []

            for item in monkey.items:
                worry_level = monkey.operation(item)

                if part == 1:
                    worry_level //= 3
                else:
                    worry_level %= lcm

                test_result = monkey.test(worry_level)

                monkeys[monkey.if_true if test_result else monkey.if_false].items.append(worry_level)
                monkey.inspected += 1

                to_remove.append(item)

            for item in to_remove:
                monkey.items.remove(item)

    return monkeys


def part_1(test: bool = False):
    return math.prod(sorted([monkey.inspected for monkey in get_monkeys(part=1, test=test)], reverse=True)[:2])


def part_2(test: bool = False):
    return math.prod(sorted([monkey.inspected for monkey in get_monkeys(part=2, test=test)], reverse=True)[:2])


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
