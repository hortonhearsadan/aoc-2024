import re

import numpy as np

from aoc_2024.utils import get_day_and_input_by_double_line, log_part_1, log_part_2, log_start


class MachineSystem:
    def __init__(self, x_1, y_1, x_2, y_2, p_x, p_y):  # noqa: PLR0913
        self.x_1 = x_1
        self.x_2 = x_2
        self.y_1 = y_1
        self.y_2 = y_2
        self.p_x = p_x
        self.p_y = p_y

    @property
    def A(self):  # noqa: N802
        return np.array([[self.x_1, self.y_1], [self.x_2, self.y_2]])

    @property
    def invA(self):  # noqa: N802
        return np.linalg.inv(self.A)

    @property
    def b(self):
        return np.array([self.p_x, self.p_y])

    def solve(self):
        return np.dot(self.invA.T, self.b)

    def int_solve(self, lb=0, ub=1e12):
        a, b = self.solve()

        ia, ib = round(a), round(b)
        if not lb <= ia <= ub >= ib >= lb:
            return None, None

        if self.solved(ia, ib):
            return ia, ib
        return None, None

    def solved(self, a, b):
        return (self.x_1 * a) + (self.x_2 * b) == self.p_x and (self.y_1 * a) + (self.y_2 * b) == self.p_y


def part_1(data, offset=0, ub=1e12):
    regex = re.compile(r".*?(\d+).*?(\d+)\n.*?(\d+).*?(\d+)\n.*?(\d+).*?(\d+)")
    total_tokens = 0
    for d in data:
        matches = re.match(regex, d)
        system = MachineSystem(*map(int, matches.groups()))
        if offset:
            system.p_y += offset
            system.p_x += offset
        x, y = system.int_solve(lb=0, ub=ub)
        if x is not None and y is not None:
            tokens = 3 * x + y
            total_tokens += tokens

    return int(total_tokens)


def run():
    d, f = get_day_and_input_by_double_line(__file__)
    #     f="""Button A: X+94, Y+34
    # Button B: X+22, Y+67
    # Prize: X=8400, Y=5400
    #
    # Button A: X+26, Y+66
    # Button B: X+67, Y+21
    # Prize: X=12748, Y=12176
    #
    # Button A: X+17, Y+86
    # Button B: X+84, Y+37
    # Prize: X=7870, Y=6450
    #
    # Button A: X+69, Y+23
    # Button B: X+27, Y+71
    # Prize: X=18641, Y=10279""".split("\n\n")

    log_start(d)
    part1 = part_1(f, ub=100)
    log_part_1(part1)

    part2 = part_1(f, 10000000000000, ub=10000000000000)
    log_part_2(part2)


if __name__ == "__main__":
    run()
