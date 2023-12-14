import os
import importlib

day_12 = importlib.import_module("advent_of_code.2022.day_12.day_12")

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# f = open(os.path.join(__location__, 'input.txt'))
# test_input = f.read().splitlines()


# def test_part_1():
#     result = day_12.part_1(test_input)

#     assert result == 31


# def test_part_2():
#     result = day_12.part_2(test_input)

#     assert result is None
