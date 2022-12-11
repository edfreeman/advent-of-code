import os
import numpy as np

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))
input = f.read().splitlines()


def part_1(input):
    raw_matrix = []

    for line in input:
        raw_matrix.append([int(i) for i in line])

    matrix = np.array(raw_matrix)

    visible_count = 0
    number_elements = matrix.shape[0]

    for i in range(1, number_elements - 1):
        for j in range(1, number_elements - 1):
            current_element = matrix[i,j]
            max_left_element = max(matrix[i, :j])
            max_right_element = max(matrix[i, (j+1):])
            max_above_element = max(matrix[:i, j])
            max_below_element = max(matrix[(i+1):, j])

            is_visible = (
                (current_element > max_left_element) or
                (current_element > max_right_element) or
                (current_element > max_above_element) or
                (current_element > max_below_element))

            if is_visible:
                visible_count += 1

    perimeter = (number_elements - 1) * 4

    visible_count += perimeter

    return visible_count


def part_2(input):
    raw_matrix = []

    for line in input:
        raw_matrix.append([int(i) for i in line])

    matrix = np.array(raw_matrix)

    number_elements = matrix.shape[0]
    scenic_scores = []

    for i in range(1, number_elements - 1):
        for j in range(1, number_elements - 1):
            current_element = matrix[i,j]

            above_offset = 0
            while i - above_offset > 0:
                above_offset += 1
                if matrix[(i-above_offset), j] < current_element:
                    continue
                else:
                    break

            below_offset = 0
            while i + below_offset < number_elements - 1:
                below_offset += 1
                if matrix[(i+below_offset), j] < current_element:
                    continue
                else:
                    break

            left_offset = 0
            while j - left_offset > 0:
                left_offset += 1
                if matrix[i, (j-left_offset)] < current_element:
                    continue
                else:
                    break

            right_offset = 0
            while j + right_offset < number_elements - 1:
                right_offset += 1
                if matrix[i, (j+right_offset)] < current_element:
                    continue
                else:
                    break

            scenic_score = above_offset * below_offset * left_offset * right_offset

            scenic_scores.append(scenic_score)

    return max(scenic_scores)


result = part_1(input)

print(result)


result = part_2(input)

print(result)
