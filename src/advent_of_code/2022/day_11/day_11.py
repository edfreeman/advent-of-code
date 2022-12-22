import os
from functools import reduce

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, 'input.txt'))
input = f.read().splitlines()


def _parse_instructions(input):
    number_of_monkeys = (len(input) + 1) // 7
    # monkey_instructions_split = [input[p:p+6] for i in range(number_of_monkeys) if (p := i*7)] # Why does this not work?
    monkey_instructions_split = [input[(i*7):(i*7)+6] for i in range(number_of_monkeys)]

    monkey_instructions_parsed = {
        int(monkey[0][-2]): {
            "items": [int(i) for i in monkey[1].split(": ")[1].split(", ")],
            "operation": monkey[2].split("= ")[1],
            "test": {
                "divisible_by": int(monkey[3].split("by ")[1]),
                "if_true_target": int(monkey[4][-1]),
                "if_false_target": int(monkey[5][-1])
            }
        }
        for monkey in monkey_instructions_split
    }

    return monkey_instructions_parsed


def part_1(input):
    monkeys = _parse_instructions(input)

    monkey_inspections = {i: 0 for i in monkeys}

    for round in range(20):
        for monkey_number, monkey_config in monkeys.items():
            items = monkey_config["items"]
            for item in items:
                func = eval("lambda old : " + monkey_config["operation"])
                new_val = func(item)
                # new_val = new_val // 3
                if new_val % monkey_config["test"]["divisible_by"] == 0:
                    monkeys[monkey_config["test"]["if_true_target"]]["items"].append(new_val)
                else:
                    monkeys[monkey_config["test"]["if_false_target"]]["items"].append(new_val)

            monkey_inspections[monkey_number] += len(items)
            monkey_config["items"] = []

    inspection_counts = list(monkey_inspections.values())

    inspection_counts.sort(reverse=True)

    top_two = inspection_counts[:2]

    result = top_two[0] * top_two[1]

    return result


def part_2(input):
    monkeys = _parse_instructions(input)
    divisible_bys = set([monkey["test"]["divisible_by"] for monkey in monkeys.values()])
    lcm = reduce(lambda a, b: a * b, divisible_bys)

    monkey_inspections = {i: 0 for i in monkeys}

    for round in range(10000):
        for monkey_number, monkey_config in monkeys.items():
            items = monkey_config["items"]
            for item in items:
                func = eval("lambda old : " + monkey_config["operation"])
                new_val = func(item)
                new_val = new_val % lcm
                if new_val % monkey_config["test"]["divisible_by"] == 0:
                    monkeys[monkey_config["test"]["if_true_target"]]["items"].append(new_val)
                else:
                    monkeys[monkey_config["test"]["if_false_target"]]["items"].append(new_val)

            monkey_inspections[monkey_number] += len(items)
            monkey_config["items"] = []

    inspection_counts = list(monkey_inspections.values())

    inspection_counts.sort(reverse=True)

    top_two = inspection_counts[:2]

    result = top_two[0] * top_two[1]

    return result

# result = part_1(input)
result = part_2(input)

print(result)
