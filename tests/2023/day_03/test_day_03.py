import os
import importlib

module = importlib.import_module("advent_of_code.2023.day_03.day_03")

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))
test_input = f.read().splitlines()


def test_part_1():
    result = module.part_1(test_input)

    assert result == 4361


# def test_part_2():
#     result = module.part_2(test_input)

#     assert result == 2286
