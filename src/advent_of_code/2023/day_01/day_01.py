import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))
input = f.read().splitlines()


def _parse_instructions(input):
    pass


def part_1():
    input_digits_extracted = []
    output_numbers = []

    for line in input:
        input_digits_extracted.append([c for c in line if ord(c) < 65])

    for digits in input_digits_extracted:
        output_numbers.append(int(''.join([digits[0], digits[-1]])))

    result = sum(output_numbers)

    print(result)


def part_2():
    number_names = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9"
    }

    calibration_values = []
    for line in input:
        current_min_index = len(line)
        current_max_index = 0
        first_value = None
        last_value = None
        for n in number_names.keys():
            if n in line:
                first_occurrence_position = line.index(n)
                if first_occurrence_position < current_min_index:
                    current_min_index = first_occurrence_position
                    first_value = n
                last_occurrence_position = line.rfind(n)
                if last_occurrence_position >= current_max_index:
                    current_max_index = last_occurrence_position
                    last_value = n
        
        calibration_value = int(number_names[first_value] + number_names[last_value])
        calibration_values.append(calibration_value)

    result = sum(calibration_values)

    print(result)

part_1()

part_2()