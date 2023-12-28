def _parse_instructions(input):
    separator_indexes = [i for i, line in enumerate(input) if line == ""]

    seeds = [int(i) for i in input[0].split(": ")[1].split(" ")]

    seeds_to_soil_map_raw = input[(separator_indexes[0] + 2):(separator_indexes[1])]
    seeds_to_soil_map = [[int(e) for e in i.split(" ")] for i in seeds_to_soil_map_raw]

    soil_to_fertilizer_map_raw = input[(separator_indexes[1] + 2):(separator_indexes[2])]
    soil_to_fertilizer_map = [[int(e) for e in i.split(" ")] for i in soil_to_fertilizer_map_raw]

    fertilizer_to_water_map_raw = input[(separator_indexes[2] + 2):(separator_indexes[3])]
    fertilizer_to_water_map = [[int(e) for e in i.split(" ")] for i in fertilizer_to_water_map_raw]

    water_to_light_map_raw = input[(separator_indexes[3] + 2):(separator_indexes[4])]
    water_to_light_map = [[int(e) for e in i.split(" ")] for i in water_to_light_map_raw]

    light_to_temperature_map_raw = input[(separator_indexes[4] + 2):(separator_indexes[5])]
    light_to_temperature_map = [[int(e) for e in i.split(" ")] for i in light_to_temperature_map_raw]

    temperature_to_humidity_map_raw = input[(separator_indexes[5] + 2):(separator_indexes[6])]
    temperature_to_humidity_map = [[int(e) for e in i.split(" ")] for i in temperature_to_humidity_map_raw]

    humidity_to_location_map_raw = input[(separator_indexes[6] + 2):]
    humidity_to_location_map = [[int(e) for e in i.split(" ")] for i in humidity_to_location_map_raw]

    def _parse_maps(map_elements):
        return [
            {
                "source_start": e[1],
                "destination_start": e[0],
                "range": e[2]
            } for e in map_elements
        ]

    seeds_to_soil_map = _parse_maps(seeds_to_soil_map)
    soil_to_fertilizer_map = _parse_maps(soil_to_fertilizer_map)
    fertilizer_to_water_map = _parse_maps(fertilizer_to_water_map)
    water_to_light_map = _parse_maps(water_to_light_map)
    light_to_temperature_map = _parse_maps(light_to_temperature_map)
    temperature_to_humidity_map = _parse_maps(temperature_to_humidity_map)
    humidity_to_location_map = _parse_maps(humidity_to_location_map)

    instructions = {
        "seeds": seeds,
        "map_instructions": {
            "seeds_to_soil": seeds_to_soil_map,
            "soil_to_fertilizer": soil_to_fertilizer_map,
            "fertilizer_to_water": fertilizer_to_water_map,
            "water_to_light": water_to_light_map,
            "light_to_temperature": light_to_temperature_map,
            "temperature_to_humidity": temperature_to_humidity_map,
            "humidity_to_location": humidity_to_location_map,
        }
    }

    return instructions


def part_1(input):
    def _get_number_from_map(number, map_name) -> int:
        map = instructions["map_instructions"][map_name]
        target_number = None
        for instruction in map:
            source_start = instruction["source_start"]
            destination_start = instruction["destination_start"]
            range = instruction["range"]
            if number >= source_start and number <= (source_start + range):
                target_number = destination_start + (number - source_start)
                return target_number

        if not target_number:
            target_number = number

        return target_number

    instructions = _parse_instructions(input)

    locations = []

    for seed in instructions["seeds"]:
        soil_number = _get_number_from_map(seed, "seeds_to_soil")
        fertilizer_number = _get_number_from_map(soil_number, "soil_to_fertilizer")
        water_number = _get_number_from_map(fertilizer_number, "fertilizer_to_water")
        light_number = _get_number_from_map(water_number, "water_to_light")
        temperature_number = _get_number_from_map(light_number, "light_to_temperature")
        humidity_number = _get_number_from_map(temperature_number, "temperature_to_humidity")
        location_number = _get_number_from_map(humidity_number, "humidity_to_location")

        locations.append(location_number)

    return min(locations)


def part_2(input):
    instructions = _parse_instructions(input)
    return None
