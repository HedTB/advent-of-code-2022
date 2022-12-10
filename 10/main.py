from typing import NamedTuple


with open("10/input.txt", "r") as file:
    lines = list(map(lambda s: s.strip().split(), file.readlines()))


class Execution(NamedTuple):
    cycle: int
    add: int


def get_signals():
    signals = [1]
    x = 1

    for parts in lines:
        signals.append(x)

        if parts[0] == "addx":
            x += int(parts[1])
            signals.append(x)

    return signals


def part_1():
    signal_strengths: list[int] = []
    pending_executions: list[Execution] = []
    x = 1

    for cycle, parts in enumerate(lines, 1):
        execution = pending_executions[0] if len(pending_executions) > 0 else None

        if execution and cycle >= execution.cycle + 2:
            print(f"{execution.add} cycle: {cycle} | execution.cycle: {execution.cycle}")
            x += execution.add

            pending_executions.remove(execution)

        print(*parts)

        if parts[0] == "addx":
            print(f"{parts[1]} {cycle} -> {cycle + 2}")
            pending_executions.append(Execution(cycle=cycle, add=int(parts[1])))

        if cycle in [20, 60, 100, 140, 180, 220]:
            signal_strengths.append(cycle * x)

    return sum(signal_strengths)


def part_1_1():
    return sum((x * get_signals()[x - 1] for x in range(20, 220 + 40, 40)))


def part_2():
    line = 40
    signals = get_signals()
    crt = ["#" if abs(position - (i % line)) <= 1 else "." for i, position in enumerate(signals)]

    for i in range(0, len(signals) // line):
        print("".join(crt[i * line : (i + 1) * line]))


print(f"Part 1: {part_1_1()}")

print("Part 2:")
part_2()
