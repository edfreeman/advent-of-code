import os
import importlib

day_10 = importlib.import_module("advent_of_code.2022.day_10.day_10")

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))
test_input = f.read().splitlines()


def test_part_1():
    result = day_10.part_1(test_input)

    assert result[0] == 13140


def test_part_2():
    _, register = day_10.part_1(test_input)

    result = day_10.part_2(register)

    assert result == (
'''##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....'''
)