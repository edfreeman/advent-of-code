import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))
input = f.read().splitlines()


def generate_structure(input: list, structure: dict, position: int):
    while position < len(input):
        line = input[position]
        if line == "$ ls":
            position += 1
            line = input[position]
            while not line.startswith("$ "):
                if line.startswith("dir"):
                    parts = line.split(" ")
                    structure[parts[1]] = {}
                else:
                    parts = line.split(" ")
                    structure[parts[1]] = int(parts[0])

                position += 1

                if position < len(input):
                    line = input[position]
                else:
                    break

        if line.startswith("$ cd "):
            destination = line.removeprefix("$ cd ")
            position += 1
            if destination == "..":
                break
            else:
                structure[destination], position = generate_structure(input, structure[destination], position)

    return structure, position


def calculate_dir_total_part_1(structure, total):
    dir_total = 0
    for item in structure:
        if isinstance(structure[item], int):
            dir_total += structure[item]
        else:
            x, total = calculate_dir_total_part_1(structure[item], total)
            dir_total += x

    if dir_total < 100000:
        total += dir_total

    return dir_total, total


def calculate_dir_total_part_2(structure, candidates, threshold):
    dir_total = 0
    for item in structure:
        if isinstance(structure[item], int):
            dir_total += structure[item]
        else:
            x, candidates = calculate_dir_total_part_2(structure[item], candidates, threshold)
            dir_total += x

    if dir_total >= threshold:
        candidates.append(dir_total)

    return dir_total, candidates


def part_1(input):
    structure = {"/": {}}
    position = 0

    full_directory_structure, _ = generate_structure(input, structure, position)

    _, full_total = calculate_dir_total_part_1(full_directory_structure, 0)

    return full_total


def part_2(input):
    structure = {"/": {}}
    position = 0

    full_directory_structure, _ = generate_structure(input, structure, position)

    outer_directory_total, _ = calculate_dir_total_part_1(full_directory_structure, 0)

    threshold = 30000000 - (70000000 - outer_directory_total)

    _, candidates = calculate_dir_total_part_2(full_directory_structure, [], threshold)

    min_dir_size = min(candidates)

    return min_dir_size


# result = part_1(input)

result = part_2(input)

print(result)
