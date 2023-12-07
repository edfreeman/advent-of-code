import os
import importlib

day_07 = importlib.import_module("advent_of_code.2022.day_07.day_07")

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))
test_input = f.read().splitlines()


def test_part_1():
    result = day_07.part_1(test_input)

    assert result == 95437


def test_part_2():
    result = day_07.part_2(test_input)

    assert result == 24933642
