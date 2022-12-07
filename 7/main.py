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

    keys = path.split("/")
    value: dict | int | None = d.get(keys.pop())

    print(keys)

    if not isinstance(value, dict):
        return value

    for key in keys:
        value = value.get(key)  # type: ignore

    return value


def part_1() -> int:
    directories = {"/": {}}
    current_path = ""

    for line in lines:
        parts = line.split()
        sub_dir = get_value_from_path(directories, current_path)

        print(current_path)
        print(sub_dir)

        if parts[0] == "$":
            if parts[1] == "cd":
                print(parts[2])

                if parts[2] == "..":
                    print("go up")
                    current_path = current_path[: current_path.rfind("/")]
                elif parts[2] == "/":
                    current_path = ""
                elif sub_dir and parts[2] not in sub_dir:
                    print("creating new sub dir")
                    directories[current_path][parts[2]] = {}
                    print(f"{current_path}{parts[2]}/")
                    current_path += f"{parts[2]}/"
                else:
                    print("appending to path")
                    current_path += f"{parts[2]}/"
        else:
            if parts[0] == "dir":
                print("dir")
                print(sub_dir)
            else:
                sub_dir[parts[1]] = parts[0]

    print(directories)

    return sum([value for value in get_nested_dict_values(directories) if value <= 100000])


def part_2() -> int:
    pass


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
