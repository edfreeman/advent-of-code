import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))
input = f.read().splitlines()


def _parse_instructions(input):
    instructions = []
    for line in input:
        instruction_split = line.split(" ")
        if len(instruction_split) == 2:
            instructions.append({"instruction": instruction_split[0], "value": int(instruction_split[1])})
        else:
            instructions.append({"instruction": instruction_split[0]})

    return instructions


def part_1(input):
    instructions = _parse_instructions(input)

    cycle = 0
    register = [1,]
    for item in instructions:
        instruction = item["instruction"]
        last_value = register[-1]
        if instruction == "noop":
            cycle += 1
            register.append(last_value)
            continue
        else:
            cycle += 2
            register.append(last_value)
            register.append(last_value + item["value"])

    checkpoints = [20, 60, 100, 140, 180, 220]
    signal_strengths = []

    for checkpoint in checkpoints:
        # Need to calculate *during* checkpoint, not *after*. So substract 1.
        signal_strengths.append(checkpoint * register[checkpoint - 1])

    total_signal_strength = sum(signal_strengths)

    return total_signal_strength, register


def part_2(register):
    image_rows = []

    for i in range(6):
        current_crt_row = ''
        for position in range(0, 40):
            register_position = register[position]
            sprite_positions = [register_position - 1, register_position, register_position + 1]
            if position in sprite_positions:
                current_crt_row += "#"
            else:
                current_crt_row += "."

        image_rows.append(current_crt_row)
        register = register[40:]

    return "\n".join(image_rows)

result, register = part_1(input)

result = part_2(register)

print(result)
