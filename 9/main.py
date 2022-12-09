from __future__ import annotations

with open("9/input.txt", "r") as file:
    lines = list(map(lambda s: s.strip().split(), file.readlines()))


class Knot(object):
    def __init__(self, previous: Knot | None = None) -> None:
        self.x = 0
        self.y = 0

        self.previous = previous

    def __repr__(self) -> str:
        return f"<x={self.x} y={self.y} previous={self.previous}>"

    def move(self, move: str, distance: int):
        if move == "R":
            self.x += distance
        elif move == "L":
            self.x -= distance
        elif move == "U":
            self.y += distance
        elif move == "D":
            self.y -= distance

    def adjacent(self, other: Knot) -> bool:
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx, ny = dx + self.x, dy + self.y

                if nx == other.x and ny == other.y:
                    return True

        return False

    def catchup(self, other: Knot):
        if self.y == other.y:
            self.move("R" if other.x > self.x else "L", 1)
        elif self.x == other.x:
            self.move("U" if other.y > self.y else "D", 1)
        else:
            self.move("U" if other.y > self.y else "D", 1)
            self.move("R" if other.x > self.x else "L", 1)


def part_1() -> int:
    positions_visited: set[tuple[int, int]] = set()
    head, tail = Knot(), Knot()

    for move, distance in lines:
        for _ in range(int(distance)):
            head.move(move, 1)

            if not tail.adjacent(head):
                tail.catchup(head)

            positions_visited.add((tail.x, tail.y))

    return len(positions_visited)


def part_2() -> int:
    positions_visited: set[tuple[int, int]] = set()
    head = Knot()
    knots = [Knot()]

    for _ in range(8):
        knot = Knot()

        knot.previous = knots[-1]
        knots.append(knot)

    for move, distance in lines:
        for _ in range(int(distance)):
            head.move(move, 1)

            current_head = head
            current_tail = knots[-1]

            while current_tail is not None:
                if not current_head.adjacent(current_tail):
                    current_tail.catchup(current_head)

                current_head = current_tail
                current_tail = current_tail.previous

            positions_visited.add((current_head.x, current_head.y))

    return len(positions_visited)


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
