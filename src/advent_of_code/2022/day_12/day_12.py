import os
import numpy as np

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# f = open(os.path.join(__location__, 'input.txt'))
# input = f.read().splitlines()


def _parse_matrix(input):
    raw_matrix = []

    for line in input:
        raw_matrix.append([i for i in line])

    matrix = np.array(raw_matrix)

    return matrix


def _get_next_element(matrix, current_position):
    current_element = matrix[current_position]

    if current_element == 'S':
        current_order = 97
    else:
        current_order = ord(current_element)

    current_row = current_position[0]
    current_column = current_position[1]

    matrix_height, matrix_width = matrix.shape

    element_above = (current_row - 1, current_column) if current_row > 0 else None
    element_below = (current_row + 1, current_column) if current_row < matrix_height - 1 else None
    element_left = (current_row, current_column - 1) if current_column > 0 else None
    element_right = (current_row, current_column + 1) if current_column < matrix_width - 1 else None
    options = {}

    options["up"] = {
        "position": element_above,
        "value": matrix[element_above] if element_above else None
    }

    options["down"] = {
        "position": element_below,
        "value": matrix[element_below] if element_below else None
    }

    options["left"] = {
        "position": element_left,
        "value": matrix[element_left] if element_left else None
    }

    options["right"] = {
        "position": element_right,
        "value": matrix[element_right] if element_right else None
    }

    max_value = max([e["value"] for e in options.values() if e["value"] and ord(e["value"]) <= current_order + 1])
    elements_with_max = ((e, options[e]["position"]) for e in options if options[e]["value"] == max_value)

    chosen_element = next(elements_with_max)
    next_direction, next_position = chosen_element[0], chosen_element[1]

    match next_direction:
        case "up":
            matrix[current_position] = 'U'
        case "down":
            matrix[current_position] = 'D'
        case "left":
            matrix[current_position] = 'L'
        case "right":
            matrix[current_position] = 'R'

    return matrix, next_position


def part_1(input):
    matrix = _parse_matrix(input)

    starting_position_element = np.where(matrix == 'S')
    ending_position_element = np.where(matrix == 'E')

    starting_position = (
        starting_position_element[0][0],
        starting_position_element[1][0]
    )

    ending_position = (
        ending_position_element[0][0],
        ending_position_element[1][0]
    )

    current_position = starting_position
    matrix[ending_position] = 'z'
    counter = 0

    while current_position != ending_position:
        matrix, next_position = _get_next_element(matrix, current_position)
        current_position = next_position
        print(counter)
        counter += 1

    return counter


# result = part_1(input)

# print(result)
