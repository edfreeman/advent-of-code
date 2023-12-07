import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))
input = f.read().splitlines()


def get_char_priority(character):
    order = ord(character)

    if order <= 90:
        priority = order - 38
    else:
        priority = order - 96

    return priority


def part_1():
    total_priority = 0

    for line in input:
        line_length = len(line)
        split = int(line_length / 2)
        parts = (line[:split], line[split:])
        common_char = next(iter(set(parts[0]) & set(parts[1])))

        total_priority += get_char_priority(common_char)

    print(total_priority)


# part_1()


def part_2():
    total_priority = 0
    lines = input

    while len(lines) > 0:
        group = lines[:3]
        common_char = next(iter(set(group[0]) & set(group[1]) & set(group[2])))
        total_priority += get_char_priority(common_char)

        new_index = len(lines) - 3

        if new_index != 0:
            lines = input[-new_index:]
        else:
            lines = []

    print(total_priority)


part_2()
