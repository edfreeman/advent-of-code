import numpy as np


def _parse_matrix(input):
    raw_matrix = []

    for line in input:
        raw_matrix.append([i for i in line])

    matrix = np.array(raw_matrix)

    return matrix


class SymbolChecker():
    def __init__(self, matrix):
        self.matrix = matrix
        self.non_symbol_cells_ords = [46] + list(range(48, 58))

    def _check_right(self, i, j):
        return True if ord(self.matrix[(i, j+1)]) not in self.non_symbol_cells_ords else False

    def _check_bottom_right(self, i, j):
        return True if ord(self.matrix[(i+1, j+1)]) not in self.non_symbol_cells_ords else False

    def _check_bottom(self, i, j):
        return True if ord(self.matrix[(i+1, j)]) not in self.non_symbol_cells_ords else False

    def _check_bottom_left(self, i, j):
        return True if ord(self.matrix[(i+1, j-1)]) not in self.non_symbol_cells_ords else False

    def _check_left(self, i, j):
        return True if ord(self.matrix[(i, j-1)]) not in self.non_symbol_cells_ords else False

    def _check_top_left(self, i, j):
        return True if ord(self.matrix[(i-1, j-1)]) not in self.non_symbol_cells_ords else False

    def _check_top(self, i, j):
        return True if ord(self.matrix[(i-1, j)]) not in self.non_symbol_cells_ords else False

    def _check_top_right(self, i, j):
        return True if ord(self.matrix[(i, j+1)]) not in self.non_symbol_cells_ords else False

    def check_adjacent_symbol(self, index):
        max_index = self.matrix.shape[0]
        i = index[0]
        j = index[1]

        if i == 0:
            if self._check_bottom(i, j):
                return True
            if j == 0:
                if self._check_right(i, j):
                    return True
                if self._check_bottom_right(i, j):
                    return True
            elif j == max_index - 1:
                if self._check_left(i, j):
                    return True
                if self._check_bottom_left(i, j):
                    return True
            else:
                if self._check_right(i, j):
                    return True
                if self._check_bottom_right(i, j):
                    return True
                if self._check_left(i, j):
                    return True
                if self._check_bottom_left(i, j):
                    return True

        elif i == 0 and j == max_index - 1:
            if self._check_bottom(i, j):
                return True
        elif i == max_index - 1 and j == 0:
            if self._check_top(i, j):
                return True
            if self._check_top_right(i, j):
                return True
            if self._check_right(i, j):
                return True
        elif i == max_index - 1 and j == max_index - 1:
            if self._check_top(i, j):
                return True
            if self._check_top_left(i, j):
                return True
            if self._check_left(i, j):
                return True
        else:
            if self._check_right(i, j):
                return True
            if self._check_bottom_right(i, j):
                return True
            if self._check_bottom(i, j):
                return True
            if self._check_left(i, j):
                return True
            if self._check_bottom_left(i, j):
                return True
            if self._check_top(i, j):
                return True
            if self._check_top_right(i, j):
                return True
            if self._check_top_left(i, j):
                return True


def part_1(input):
    matrix = _parse_matrix(input)
    number_elements = matrix.shape[0]
    symbol_checker = SymbolChecker(matrix)

    for i in range(number_elements):
        parsing_number = False
        for j in range(number_elements):
            element = matrix[i, j]
            element_order = ord(element)
            if (element_order >= 48) and (element_order <= 57):
                if not parsing_number:
                    parsing_number = True
                    current_number_details = {
                        "chars": [],
                        "positions": [],
                        "is_part_number": None
                    }

                current_number_details["chars"].append(element)
                current_number_details["positions"].append((i, j))
                if not current_number_details["is_part_number"]:
                    current_number_details["is_part_number"] = symbol_checker.check_adjacent_symbol(
                        (i, j)
                    )
            else:
                parsing_number = False

    return False


def part_2(input):
    instructions = _parse_matrix(input)
    return instructions
