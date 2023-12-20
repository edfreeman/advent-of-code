import os
import importlib

module = importlib.import_module("advent_of_code.2023.day_04.day_04")

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))
test_input = f.read().splitlines()


def test_part_1():
    result, _ = module.part_1(test_input)

    assert result == 13


def test_part_2():
    result = module.part_2(test_input)

    assert result == 30
