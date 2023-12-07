import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))

input = f.read().splitlines()


def part_1():
    total = 0

    for round in input:
        match round:
            case 'A X':
                total += (1 + 3)
            case 'A Y':
                total += (2 + 6)
            case 'A Z':
                total += (3 + 0)
            case 'B X':
                total += (1 + 0)
            case 'B Y':
                total += (2 + 3)
            case 'B Z':
                total += (3 + 6)
            case 'C X':
                total += (1 + 6)
            case 'C Y':
                total += (2 + 0)
            case 'C Z':
                total += (3 + 3)

    print(total)


part_1()


def part_2():
    total = 0

    for round in input:
        match round:
            case 'A X':
                total += (3 + 0)
            case 'A Y':
                total += (1 + 3)
            case 'A Z':
                total += (2 + 6)
            case 'B X':
                total += (1 + 0)
            case 'B Y':
                total += (2 + 3)
            case 'B Z':
                total += (3 + 6)
            case 'C X':
                total += (2 + 0)
            case 'C Y':
                total += (3 + 3)
            case 'C Z':
                total += (1 + 6)

    print(total)


part_2()
