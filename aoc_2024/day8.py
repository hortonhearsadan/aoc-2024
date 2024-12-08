from collections import defaultdict

from aoc_2024.utils import get_day_and_input_by_line, log_part_1, log_part_2, log_start


def part_1(data):
    x = len(data[0])
    y = len(data)

    antennae_by_type = defaultdict(list)
    for j, row in enumerate(data):
        for i, char in enumerate(row):
            if char != ".":
                pos = complex(i, -j)
                antennae_by_type[char].append(pos)
    nodes = set()
    for _ant, places in antennae_by_type.items():
        for p in places:
            for q in places:
                if p == q:
                    continue

                diff = p - q

                antinode = p + diff
                if x > antinode.real >= 0 >= antinode.imag > -y:
                    nodes.add(antinode)

    return len(nodes)


def part_2(data):
    x = len(data[0])
    y = len(data)

    antennae_by_type = defaultdict(list)
    for j, row in enumerate(data):
        for i, char in enumerate(row):
            if char != ".":
                pos = complex(i, -j)
                antennae_by_type[char].append(pos)
    nodes = set()
    for _ant, places in antennae_by_type.items():
        for p in places:
            nodes.add(p)
            for q in places:
                if p == q:
                    continue

                diff = p - q

                antinode = p + diff
                while x > antinode.real >= 0 >= antinode.imag > -y:
                    nodes.add(antinode)
                    antinode += diff

    return len(nodes)


def run():
    d, f = get_day_and_input_by_line(__file__)
    #     f = """............
    # ........0...
    # .....0......
    # .......0....
    # ....0.......
    # ......A.....
    # ............
    # ............
    # ........A...
    # .........A..
    # ............
    # ............""".split("\n")
    #     f="""..........
    # ..........
    # ..........
    # ....a.....
    # ........a.
    # .....a....
    # ..........
    # ..........
    # ..........
    # ..........""".split("\n")

    log_start(d)
    part1 = part_1(f)
    log_part_1(part1)

    part2 = part_2(f)
    log_part_2(part2)


if __name__ == "__main__":
    run()
