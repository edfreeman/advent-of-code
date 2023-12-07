import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))
input = f.read().splitlines()


def _parse_instructions(input):
    instructions = []
    for line in input:
        instruction_split = line.split(" ")

    return instructions


def part_1(input):
    instructions = _parse_instructions(input)



result = part_1(input)

print(result)