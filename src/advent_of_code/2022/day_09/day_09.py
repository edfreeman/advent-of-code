import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))
input = f.read().splitlines()


def _parse_instructions(input):
    instructions = []
    for line in input:
        instruction_groups = line.split(" ")
        instructions.append({"direction": instruction_groups[0], "steps": int(instruction_groups[1])})

    return instructions


def _update_next_knot(current_leader_position, current_follower_position):
    l_x_pos = current_leader_position[0]
    l_y_pos = current_leader_position[1]
    f_x_pos = current_follower_position[0]
    f_y_pos = current_follower_position[1]

    difference = (l_x_pos - f_x_pos, l_y_pos - f_y_pos)

    new_f_pos = current_follower_position

    match difference:
        case (0, 2):
            new_f_pos = (f_x_pos, f_y_pos + 1)
        case (1, 2) | (2, 1) | (2, 2):
            new_f_pos = (f_x_pos + 1, f_y_pos + 1)
        case (2, 0):
            new_f_pos = (f_x_pos + 1, f_y_pos)
        case (2, -1) | (1, -2) | (2, -2):
            new_f_pos = (f_x_pos + 1, f_y_pos - 1)
        case (0, -2):
            new_f_pos = (f_x_pos, f_y_pos - 1)
        case (-1, -2) | (-2, -1) | (-2, -2):
            new_f_pos = (f_x_pos - 1, f_y_pos - 1)
        case (-2, 0):
            new_f_pos = (f_x_pos - 1, f_y_pos)
        case (-2, 1) | (-1, 2) | (-2, 2):
            new_f_pos = (f_x_pos - 1, f_y_pos + 1)

    return new_f_pos


def part_1(input):
    instructions = _parse_instructions(input)

    h_positions = [(0, 0),]
    t_positions = [(0, 0),]

    for instruction in instructions:
        direction = instruction["direction"]
        steps_range = range(instruction["steps"])
        match direction:
            case "U":
                for step in steps_range:
                    last_h_position = h_positions[-1]
                    new_h_position = (last_h_position[0], last_h_position[1] + 1)
                    h_positions.append(new_h_position)

                    next_t_pos = _update_next_knot(new_h_position, t_positions[-1])
                    t_positions.append(next_t_pos)
            case "R":
                for step in steps_range:
                    last_h_position = h_positions[-1]
                    new_h_position = (last_h_position[0] + 1, last_h_position[1])
                    h_positions.append(new_h_position)

                    next_t_pos = _update_next_knot(new_h_position, t_positions[-1])
                    t_positions.append(next_t_pos)
            case "D":
                for step in steps_range:
                    last_h_position = h_positions[-1]
                    new_h_position = (last_h_position[0], last_h_position[1] - 1)
                    h_positions.append(new_h_position)

                    next_t_pos = _update_next_knot(new_h_position, t_positions[-1])
                    t_positions.append(next_t_pos)
            case "L":
                for step in steps_range:
                    last_h_position = h_positions[-1]
                    new_h_position = (last_h_position[0] - 1, last_h_position[1])
                    h_positions.append(new_h_position)

                    next_t_pos = _update_next_knot(new_h_position, t_positions[-1])
                    t_positions.append(next_t_pos)

    number_positions = len(set(t_positions))

    return number_positions


def part_2(input):
    instructions = _parse_instructions(input)

    h_positions = [(0, 0),]
    follower_positions = {i: [(0, 0),] for i in range(1, 10)}

    for instruction in instructions:
        direction = instruction["direction"]
        steps_range = range(instruction["steps"])
        match direction:
            case "U":
                for step in steps_range:
                    last_h_position = h_positions[-1]
                    new_h_position = (last_h_position[0], last_h_position[1] + 1)
                    h_positions.append(new_h_position)

                    leader_positions = h_positions[-2:]
                    i = 1
                    while (leader_positions[1] != leader_positions[0]) & (i < 10):
                        next_follower_pos = _update_next_knot(leader_positions[1], follower_positions[i][-1])
                        follower_positions[i].append(next_follower_pos)

                        leader_positions = follower_positions[i][-2:]
                        i += 1

            case "R":
                for step in steps_range:
                    last_h_position = h_positions[-1]
                    new_h_position = (last_h_position[0] + 1, last_h_position[1])
                    h_positions.append(new_h_position)

                    leader_positions = h_positions[-2:]
                    i = 1
                    while (leader_positions[1] != leader_positions[0]) & (i < 10):
                        next_follower_pos = _update_next_knot(leader_positions[1], follower_positions[i][-1])
                        follower_positions[i].append(next_follower_pos)

                        leader_positions = follower_positions[i][-2:]
                        i += 1
            case "D":
                for step in steps_range:
                    last_h_position = h_positions[-1]
                    new_h_position = (last_h_position[0], last_h_position[1] - 1)
                    h_positions.append(new_h_position)

                    leader_positions = h_positions[-2:]
                    i = 1
                    while (leader_positions[1] != leader_positions[0]) & (i < 10):
                        next_follower_pos = _update_next_knot(leader_positions[1], follower_positions[i][-1])
                        follower_positions[i].append(next_follower_pos)

                        leader_positions = follower_positions[i][-2:]
                        i += 1
            case "L":
                for step in steps_range:
                    last_h_position = h_positions[-1]
                    new_h_position = (last_h_position[0] - 1, last_h_position[1])
                    h_positions.append(new_h_position)

                    leader_positions = h_positions[-2:]
                    i = 1
                    while (leader_positions[1] != leader_positions[0]) & (i < 10):
                        next_follower_pos = _update_next_knot(leader_positions[1], follower_positions[i][-1])
                        follower_positions[i].append(next_follower_pos)

                        leader_positions = follower_positions[i][-2:]
                        i += 1

    number_positions = len(set(follower_positions[9]))

    return number_positions


# result = part_1(input)

result = part_2(input)

print(result)
