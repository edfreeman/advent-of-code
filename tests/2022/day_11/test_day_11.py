import os
import importlib

day_11 = importlib.import_module("advent_of_code.2022.day_11.day_11")

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))
test_input = f.read().splitlines()


def test_part_1():
    result = day_11.part_1(test_input)

    assert result == 10605


def test_part_2():
    result = day_11.part_2(test_input)

    assert result == 2713310158
