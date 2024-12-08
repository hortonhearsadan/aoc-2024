from loguru import logger

from aoc_2024.utils import get_day_and_input, by_line

def operate(total,operands,concat = False):
    if total < 0:
        return False
    if total == 0 and operands ==[]:
        return True
    elif total !=0 and operands == []:
        return False
    op = operands.pop()

    d,r = divmod(total,op)
    if r ==0:
        mul = operate(d,operands[:],concat)
    else:
        mul = False
    if concat:
        s_total = str(total)
        s_op = str(op)
        if len(s_total) <= len(s_op):
            con = False
        elif s_total[-len(s_op):] == s_op:
            con = operate(int(s_total[:-len(s_op)]),operands[:],concat)
        else:
            con = False

    else:
        con = False

    return mul or con or operate(total - op, operands[:],concat)

def part_1(data):

    sums = 0
    for equation in by_line(data):
        total,operands = equation.split(":")
        total = int(total)
        operands = [int(o) for o in operands.strip().split(" ")]

        if operate(total,operands,False):
            sums+= total

    return sums



def part_2(data):
    sums = 0
    for equation in by_line(data):
        total, operands = equation.split(":")
        total = int(total)
        operands = [int(o) for o in operands.strip().split(" ")]

        if operate(total, operands, concat=True):
            sums += total

    return sums


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
    part1 = part_1(f)
    logger.info(f"Part 1: {part1}")

    # f = """
    # 156: 15 6
    # 7290: 6 8 6 15
    # 192: 17 8 14
    # """
    part2 = part_2(f)
    logger.info(f"Part 2: {part2}")

if __name__ == '__main__':
    run()
