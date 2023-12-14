def _parse_instructions(input):
    instructions = {}
    for line in input:
        game, sets = line.split(": ")
        game_number = game[5:]
        sets_split = sets.split("; ")
        sets_parsed = []
        for ss in sets_split:
            combos = {}
            colour_pull = ss.split(", ")
            [combos.update({v[1]: int(v[0])}) for cp in colour_pull if (v := cp.split(" "))]
            sets_parsed.append(combos)

        instructions.update({game_number: sets_parsed})

    return instructions


def part_1(input):
    instructions = _parse_instructions(input)
    limits = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    possible_games = []
    for game in instructions.keys():
        max_red = max([e["red"] for e in instructions[game] if e.get("red")])
        max_green = max([e["green"] for e in instructions[game] if e.get("green")])
        max_blue = max([e["blue"] for e in instructions[game] if e.get("blue")])

        if (max_red <= limits["red"]) and (max_green <= limits["green"]) and (max_blue <= limits["blue"]):
            possible_games.append(int(game))

    return sum(possible_games)


def part_2(input):
    instructions = _parse_instructions(input)

    powers = []
    for game in instructions.keys():
        max_red = max([e["red"] for e in instructions[game] if e.get("red")])
        max_green = max([e["green"] for e in instructions[game] if e.get("green")])
        max_blue = max([e["blue"] for e in instructions[game] if e.get("blue")])

        power = max_red * max_green * max_blue
        powers.append(power)

    return sum(powers)
