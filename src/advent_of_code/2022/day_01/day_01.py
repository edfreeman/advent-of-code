import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def part_1():
    f = open(os.path.join(__location__, 'input.txt'))

    input = f.read().splitlines()

    groups = []
    current_group = []

    for element in input:
        if element == '':
            groups.append(current_group)
            current_group = []
            continue

        current_group.append(int(element))

    totals = [sum(g) for g in groups]

    max_cals = max(totals)

    print(max_cals)

    return totals


def part_2():
    totals: list = part_1()

    totals.sort(reverse=True)

    top_three_cals = sum(totals[:3])

    print(top_three_cals)
