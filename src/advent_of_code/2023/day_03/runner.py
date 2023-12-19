import os
import day_03 as module

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))
input = f.read().splitlines()

print("Part 1 Answer: " + str(module.part_1(input)))
print("Part 2 Answer: " + str(module.part_2(input)))
