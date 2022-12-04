import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))
input = f.read().splitlines()

groups = [(
    list(range(int(o[0].split("-")[0]), int(o[0].split("-")[1]) + 1)),
    list(range(int(o[1].split("-")[0]), int(o[1].split("-")[1]) + 1))
) for line in input if (o := line.split(','))]


def part_1():
    counter = 0

    for g in groups:
        g1 = set(g[0])
        g2 = set(g[1])

        if g1.issubset(g2) or g1.issuperset(g2):
            counter += 1

    print(counter)


part_1()


def part_2():
    counter = 0

    for g in groups:
        g1 = set(g[0])
        g2 = set(g[1])

        if g1.isdisjoint(g2):
            continue

        counter += 1

    print(counter)


part_2()
