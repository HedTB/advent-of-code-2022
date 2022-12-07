from collections import defaultdict
from pathlib import Path


with open("7/input.txt", "r") as file:
    lines = list(map(lambda s: s.strip(), file.readlines()))


def get_nested_dict_values(d):
    for v in d.values():
        if isinstance(v, dict):
            yield from get_nested_dict_values(v)
        else:
            yield v


def get_value_from_path(d: dict, path: str):
    if not path:
        return d["/"]

    keys = path.rstrip("/").split("/")
    value: dict | int | None = d["/"].get(keys.pop())

    if isinstance(value, dict) and len(keys) > 0:
        for key in keys:
            value = value.get(key)  # type: ignore

    return value


def part_1() -> int:
    directories = {"/": {}}
    current_path = ""
    current_dir = get_value_from_path(directories, current_path)

    for line in lines:
        parts = line.split()

        if not isinstance(current_dir, dict):
            raise RuntimeError("current dir is not a dict")

        if parts[0] == "$":
            if parts[1] == "cd":
                print(parts[2])

                if parts[2] == "..":
                    print("go up")
                    current_path = current_path[: current_path.rfind("/")]
                elif parts[2] == "/":
                    current_path = ""
                elif parts[2] not in current_dir:
                    print("creating new sub dir")
                    current_dir[parts[2]] = {}
                    print(f"{current_path}{parts[2]}/")
                    current_path += f"{parts[2]}/"
                else:
                    print("appending to path")
                    current_path += f"{parts[2]}/"
        else:
            if parts[0] == "dir":
                pass
            else:
                print(f"found file of size {parts[0]}")
                current_dir[parts[1]] = parts[0]

    return sum(
        [int(value) for value in get_nested_dict_values(directories) if isinstance(value, str) and int(value) <= 100000]
    )


def get_directory_sizes() -> dict:
    sizes = {}
    directory_sizes = defaultdict(int)
    path_trace = [""]

    for line in lines:
        if line == "$ cd ..":
            path_trace.pop()
        elif line.startswith("$ cd"):
            path_trace.append(line[5:])
        elif line[0].isnumeric():
            parts = line.split()
            sizes["/".join(path_trace + [parts[1]])] = int(parts[0])

    for path, size in sizes.items():
        for directory in Path(path).parents:
            directory_sizes[str(directory)] += size

    return directory_sizes


def part_1_1() -> int:
    directory_sizes = get_directory_sizes()

    return sum(size for size in directory_sizes.values() if size <= 100000)


def part_2() -> int:
    directory_sizes = get_directory_sizes()
    free_space = 70000000 - directory_sizes["\\"]

    return next(size for size in sorted(directory_sizes.values()) if size >= 30000000 - free_space)


print(f"Part 1: {part_1_1()}")
print(f"Part 2: {part_2()}")
