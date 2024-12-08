import re

from aoc_2024.utils import get_day_and_input, log_part_1, log_part_2, log_start


def part_1(data):
    rx = re.compile("mul\\((\\d{1,3}),(\\d{1,3})\\)")
    return sum(multiply(r) for r in re.findall(rx, data))


def part_2(data):
    rx = "(mul)\\((\\d{1,3}),(\\d{1,3})\\)|(do)\\(\\)|(don't)\\(\\)"
    enabled = True
    total = 0
    for m in re.findall(rx, data):
        if "mul" in m and enabled:
            total += multiply(m[1:3])

        elif "do" in m:
            enabled = True
        elif "don't" in m:
            enabled = False
    return total


def multiply(match):
    return int(match[0]) * int(match[1])


def run():
    d, f = get_day_and_input(__file__)
    log_start(d)
    part1 = part_1(f)
    log_part_1(part1)

    part2 = part_2(f)
    log_part_2(part2)


if __name__ == "__main__":
    run()
