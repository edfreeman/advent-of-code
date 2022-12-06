import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))
input = f.read().rstrip()


def part_1():
    marker = 4
    while True:
        current_buffer = input[marker-4:marker]

        if len(current_buffer) == len(set(current_buffer)):
            print(marker)
            break

        marker += 1


part_1()


def part_2():
    marker = 14
    while True:
        current_buffer = input[marker-14:marker]

        if len(current_buffer) == len(set(current_buffer)):
            print(marker)
            break

        marker += 1


part_2()
