import collections
import math

with open("12/input.txt", "r") as file:
    main_heightmap = list(map(lambda s: s.strip(), file.readlines()))

with open("12/test_input.txt", "r") as file:
    test_heightmap = list(map(lambda s: s.strip(), file.readlines()))


def find(heightmap: list[str], letter: str) -> list[tuple[int, int]]:
    rows, columns = len(heightmap), len(heightmap[0])

    return [(row, column) for row in range(rows) for column in range(columns) if heightmap[row][column] == letter]


def get_height(heightmap: list[str], row: int, column: int) -> int:
    element = heightmap[row][column]

    if element == "S":
        return ord("a")
    elif element == "E":
        return ord("z")

    return ord(element)


def get_shortest_path(heightmap: list[str], start_row: int, start_column: int, exit_row: int, exit_column: int):
    rows, columns = len(heightmap), len(heightmap[0])
    steps = [[math.inf] * columns for _ in range(rows)]
    steps[start_row][start_column] = 0

    deque = collections.deque([(start_row, start_column)])

    while deque:
        row, column = deque.popleft()

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, column + dc

            if (
                0 <= nr < rows
                and 0 <= nc < columns
                and steps[nr][nc] == math.inf
                and get_height(heightmap, nr, nc) <= get_height(heightmap, row, column) + 1
            ):
                steps[nr][nc] = steps[row][column] + 1
                deque.append((nr, nc))

    return steps[exit_row][exit_column]


def get_args(test: bool = False) -> tuple[list[str], int, int, int, int]:
    heightmap = test_heightmap if test else main_heightmap

    start_row, start_column = find(heightmap, "S")[0]
    exit_row, exit_column = find(heightmap, "E")[0]

    return heightmap, start_row, start_column, exit_row, exit_column


def part_1(test: bool = False):
    return get_shortest_path(*get_args(test))


def part_2(test: bool = False):
    heightmap, *args, exit_row, exit_column = get_args(test)

    return min(get_shortest_path(heightmap, ra, ca, exit_row, exit_column) for ra, ca in find(heightmap, "a"))


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
