import numpy as np
import pandas as pd


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
        return True if ord(self.matrix[(i-1, j+1)]) not in self.non_symbol_cells_ords else False

    def check_adjacent_symbol(self, index):
        i = index[0]
        j = index[1]

        if (
            self._check_right(i, j) or
            self._check_bottom_right(i, j) or
            self._check_bottom(i, j) or
            self._check_bottom_left(i, j) or
            self._check_left(i, j) or
            self._check_top_left(i, j) or
            self._check_top(i, j) or
            self._check_top_right(i, j)
        ):
            return True


class SymbolChecker2():
    def __init__(self, matrix):
        self.matrix = matrix
        self.asterisk_order = 42

    def _check_right(self, i, j):
        return (i, j+1) if ord(self.matrix[(i, j+1)]) == 42 else None

    def _check_bottom_right(self, i, j):
        return (i+1, j+1) if ord(self.matrix[(i+1, j+1)]) == 42 else None

    def _check_bottom(self, i, j):
        return (i+1, j) if ord(self.matrix[(i+1, j)]) == 42 else None

    def _check_bottom_left(self, i, j):
        return (i+1, j-1) if ord(self.matrix[(i+1, j-1)]) == 42 else None

    def _check_left(self, i, j):
        return (i, j-1) if ord(self.matrix[(i, j-1)]) == 42 else None

    def _check_top_left(self, i, j):
        return (i-1, j-1) if ord(self.matrix[(i-1, j-1)]) == 42 else None

    def _check_top(self, i, j):
        return (i-1, j) if ord(self.matrix[(i-1, j)]) == 42 else None

    def _check_top_right(self, i, j):
        return (i-1, j+1) if ord(self.matrix[(i-1, j+1)]) == 42 else None

    def check_adjacent_symbol(self, index):
        i = index[0]
        j = index[1]

        return (
            self._check_right(i, j) or
            self._check_bottom_right(i, j) or
            self._check_bottom(i, j) or
            self._check_bottom_left(i, j) or
            self._check_left(i, j) or
            self._check_top_left(i, j) or
            self._check_top(i, j) or
            self._check_top_right(i, j)
        )


def part_1(input):
    matrix = _parse_matrix(input)
    number_elements = matrix.shape[0]
    padded_matrix = np.pad(matrix, 1, constant_values='.')
    symbol_checker = SymbolChecker(padded_matrix)
    all_parts = []

    for i in range(1, number_elements + 2):
        parsing_number = False
        for j in range(1, number_elements + 2):
            element = padded_matrix[i, j]
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
                if parsing_number and current_number_details["is_part_number"]:
                    current_number_details["part_number"] = int(''.join(current_number_details["chars"]))
                    all_parts.append(current_number_details)
                parsing_number = False

    part_numbers = [p["part_number"] for p in all_parts]

    return sum(part_numbers)


def part_2(input):
    matrix = _parse_matrix(input)
    number_elements = matrix.shape[0]
    padded_matrix = np.pad(matrix, 1, constant_values='.')
    symbol_checker = SymbolChecker2(padded_matrix)
    all_parts = []

    for i in range(1, number_elements + 2):
        parsing_number = False
        for j in range(1, number_elements + 2):
            element = padded_matrix[i, j]
            element_order = ord(element)
            if (element_order >= 48) and (element_order <= 57):
                if not parsing_number:
                    parsing_number = True
                    current_number_details = {
                        "chars": [],
                        "asterisk_position": None
                    }

                current_number_details["chars"].append(element)
                if not current_number_details["asterisk_position"]:
                    current_number_details["asterisk_position"] = symbol_checker.check_adjacent_symbol(
                        (i, j)
                    )
            else:
                if parsing_number and current_number_details["asterisk_position"]:
                    current_number_details["part_number"] = int(''.join(current_number_details["chars"]))
                    all_parts.append({k: current_number_details[k] for k in ("asterisk_position", "part_number")})
                parsing_number = False

    df = pd.DataFrame(all_parts)

    df_grouped = df.groupby("asterisk_position").agg(
        count=("part_number", "count"),
        prod=("part_number", "prod")
    )

    gears = df_grouped.loc[df_grouped["count"] == 2]

    return gears["prod"].sum()
