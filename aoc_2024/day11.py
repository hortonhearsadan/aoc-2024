import math
from collections import defaultdict
from functools import cache

from aoc_2024.utils import get_day_and_input, log_part_1, log_part_2, log_start


@cache
def get_keys(k):
    if k == 0:
        return (1,)
    digits = math.floor(math.log10(k)) + 1
    if digits % 2 == 0:
        e = 10 ** (digits // 2)
        return divmod(k, e)
    return (k * 2024,)


def part_1(data, blinks):
    stones = {}
    for num in data.strip().split(" "):
        stones[int(num)] = 1

    for _ in range(blinks):
        new = defaultdict(int)
        for k, v in stones.items():
            keys = get_keys(k)
            for key in keys:
                new[key] += v

        stones = new

    return sum(stones.values())


def run():
    d, f = get_day_and_input(__file__)
    log_start(d)
    part1 = part_1(f, 25)
    log_part_1(part1)
    part2 = part_1(f, 75)
    log_part_2(part2)


if __name__ == "__main__":
    run()
