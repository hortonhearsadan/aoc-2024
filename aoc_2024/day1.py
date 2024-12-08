from collections import Counter
from heapq import heapify, heappop, heappush

from aoc_2024.utils import get_day_and_input_by_line, log_part_1, log_part_2, log_start


def part_1(data):
    left = []
    right = []
    heapify(left)
    heapify(right)
    for line in data:
        x, y = map(int, line.split("   "))
        heappush(left, x)
        heappush(right, y)

    total = 0
    while left:
        a = heappop(left)
        b = heappop(right)
        total += abs(a - b)
    return total


def part_2(data):
    left = []
    right = []

    for line in data:
        x, y = map(int, line.split("   "))
        left.append(x)
        right.append(y)

    c = Counter(right)
    total = 0
    for num in left:
        total += num * c.get(num, 0)

    return total


def run():
    d, f = get_day_and_input_by_line(__file__)
    log_start(d)
    part1 = part_1(f)
    log_part_1(part1)

    part2 = part_2(f)
    log_part_2(part2)


if __name__ == "__main__":
    run()
