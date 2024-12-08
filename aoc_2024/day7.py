from loguru import logger

from aoc_2024.utils import get_day_and_input, by_line


def operate(total, operands, concat=False):
    if total < 0:
        return False
    if total == 0 and operands == []:
        return True
    elif total != 0 and operands == []:
        return False
    op = operands.pop()

    d, r = divmod(total, op)
    if r == 0:
        if operate(d, operands[:], concat):
            return True

    if concat:
        s_total = str(total)
        s_op = str(op)
        if len(s_total) > len(s_op) and s_total[-len(s_op):] == s_op:
            if operate(int(s_total[: -len(s_op)]), operands[:], concat):
                return True

    return operate(total - op, operands[:], concat)


def parse(data):
    lines = []
    for equation in by_line(data):
        total, operands = equation.split(":")
        total = int(total)
        operands = [int(o) for o in operands.strip().split(" ")]
        lines.append((total, operands))
    return lines


def part_1(data):
    return sum(total for total, operands in data if operate(total, operands[:]))


def part_2(data):
    return sum(
        total for total, operands in data if operate(total, operands[:], concat=True)
    )


def run():
    d, f = get_day_and_input(__file__)
    # f = """
    # 190: 10 19
    # 3267: 81 40 27
    # 83: 17 5
    # 156: 15 6
    # 7290: 6 8 6 15
    # 161011: 16 10 13
    # 192: 17 8 14
    # 21037: 9 7 18 13
    # 292: 11 6 16 20"""
    logger.info(f"Starting Day {d}")
    dat = parse(f)
    part1 = part_1(dat)
    logger.info(f"Part 1: {part1}")

    # f = """
    # 156: 15 6
    # 7290: 6 8 6 15
    # 192: 17 8 14
    # """
    part2 = part_2(dat)
    logger.info(f"Part 2: {part2}")


if __name__ == "__main__":
    run()
