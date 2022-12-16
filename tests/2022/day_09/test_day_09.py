import os
import importlib

day_09 = importlib.import_module("advent_of_code.2022.day_09.day_09")

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f1 = open(os.path.join(__location__, 'input_1.txt'))
f2 = open(os.path.join(__location__, 'input_2.txt'))
test_input_1 = f1.read().splitlines()
test_input_2 = f2.read().splitlines()


def test_part_1():
    result = day_09.part_1(test_input_1)

    assert result == 13


def test_1_part_2():
    result = day_09.part_2(test_input_1)

    assert result == 1


def test_2_part_2():
    result = day_09.part_2(test_input_2)

    assert result == 36
