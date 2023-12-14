import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))
input = f.read().splitlines()


def parse_input():
    line_break = input.index('')

    data = input[:(line_break - 1)]
    data.reverse()

    instructions_input = input[(line_break + 1):]

    stacks = {}

    for i in range(0, 9):
        stacks[i+1] = [val for row in data if (val := row[(i*4 + 1)]) and val != ' ']

    instructions = []

    for row in instructions_input:
        steps = {}
        steps["move"] = int(row[5:-12])
        steps["from"] = int(row[-6])
        steps["to"] = int(row[-1])

        instructions.append(steps)

    return stacks, instructions


stacks, instructions = parse_input()


def part_1(stacks, instructions):
    for instruction in instructions:
        moves = instruction["move"]
        from_bin = instruction["from"]
        to_bin = instruction["to"]
        for i in range(1, moves+1):
            stacks[to_bin].append(stacks[from_bin].pop())

    result = [stacks[i][-1] for i in range(1, len(stacks) + 1)]

    result_single_string = "".join(result)

    print(result_single_string)


# part_1(stacks, instructions)


def part_2(stacks, instructions):
    for instruction in instructions:
        moves = instruction["move"]
        from_bin = instruction["from"]
        to_bin = instruction["to"]

        crates_to_move = stacks[from_bin][-moves:]
        stacks[to_bin].extend(crates_to_move)
        stacks[from_bin] = stacks[from_bin][:-moves]

    result = [stacks[i][-1] for i in range(1, len(stacks) + 1)]

    result_single_string = "".join(result)

    print(result_single_string)


part_2(stacks, instructions)
