def _parse_instructions(input):
    instructions = {}
    for line in input:
        card, numbers = line.split(": ")
        card_number = card[5:]
        winning_numbers, my_numbers = numbers.split(" | ")
        winning_numbers_parsed = [n for n in winning_numbers.split(" ") if n != '']
        my_numbers_parsed = [n for n in my_numbers.split(" ") if n != '']

        instructions.update(
            {
                card_number: {
                    'winning_numbers': winning_numbers_parsed,
                    'my_numbers': my_numbers_parsed
                }
            }
        )

    return instructions


def part_1(input):
    instructions = _parse_instructions(input)

    matched_nums = [len(set(cn['winning_numbers']).intersection(cn['my_numbers'])) for cn in instructions.values()]

    matched_nums_expon = [2 ** (cm - 1) for cm in matched_nums if cm != 0]
    return sum(matched_nums_expon), matched_nums


def part_2(input):
    _, matched_nums = part_1(input)
    number_cards = len(matched_nums)
    counter = dict(zip(range(1, number_cards + 1), [0] * number_cards))

    for i in range(1, number_cards + 1):
        counter[i] += 1
        for _ in range(counter[i]):
            for j in range(1, matched_nums[i-1] + 1):
                counter[i+j] += 1

    return sum(counter.values())
