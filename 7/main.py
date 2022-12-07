with open("7/input.txt", "r") as file:
    lines = list(map(lambda s: s.strip(), file.readlines()))


def get_nested_dict_values(d):
    for v in d.values():
        if isinstance(v, dict):
            yield from get_nested_dict_values(v)
        else:
            yield v


def part_1() -> int:
    directories = {"/": {}}
    current_path = "/"

    for line in lines:
        parts = line.split()

        if parts[0] == "$":
            if parts[1] == "cd":
                if parts[2] == "..":
                    current_path = current_path[: current_path.rfind("/")]
                elif parts[2] not in directories[current_path]:
                    directories[current_path][parts[2]] = {}
                else:
                    current_path += f"/{parts[2]}"
        else:
            if parts[0] == "dir":

    return sum([value for value in get_nested_dict_values(directories) if value <= 100000])


def part_2() -> int:
    pass


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
