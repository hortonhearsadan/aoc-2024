from collections import defaultdict

from aoc_2024.utils import by_line, get_day_and_input, log_part_1, log_part_2, log_start

OBSTACLE = "#"
GUARDS = ("^", "V", ">", "<")


def part_1(data):
    obstacles = set()

    i = j = 0
    pos = complex(0, 0)

    for line in by_line(data):
        i = 0
        for char in line:
            if char == OBSTACLE:
                obstacles.add(complex(i, j))
            elif char in GUARDS:
                pos = complex(i, j)
                match char:
                    case "^":
                        direction = 1j
                    case ">":
                        direction = 1
                    case "<":
                        direction = -1
                    case "V":
                        direction = -1j

            i += 1
        j -= 1
    max_i = i - 1
    min_j = j + 1

    turn = -1j

    positions = {pos}
    while max_i >= pos.real >= 0 >= pos.imag >= min_j:
        positions.add(pos)
        new_pos = pos + direction
        if new_pos in obstacles:
            direction *= turn
        else:
            pos = new_pos
    return positions


def get_next_obstacle(pos, direction, new_obstacles_by_real, new_obstacles_by_imag):
    obs = 9999999 + 999999j

    try:
        if direction == 1:
            return complex(
                min(o.real for o in new_obstacles_by_imag if o.real > pos.real),
                pos.imag,
            )
        if direction == -1:
            return complex(
                max(o.real for o in new_obstacles_by_imag if o.real < pos.real),
                pos.imag,
            )
        if direction == -1j:
            return complex(
                pos.real,
                max(o.imag for o in new_obstacles_by_real if o.imag < pos.imag),
            )
        if direction == 1j:
            return complex(
                pos.real,
                min(o.imag for o in new_obstacles_by_real if o.imag > pos.imag),
            )
    except ValueError:
        return obs


def part_2(data, poss):
    obstacles = set()

    i = j = 0
    start_pos = complex(0, 0)

    for line in by_line(data):
        i = 0
        for char in line:
            if char == OBSTACLE:
                obstacles.add(complex(i, j))
            elif char in GUARDS:
                start_pos = complex(i, j)
                match char:
                    case "^":
                        start_dir = 1j
                    case ">":
                        start_dir = 1
                    case "<":
                        start_dir = -1
                    case "V":
                        start_dir = -1j

            i += 1
        j -= 1
    max_i = i - 1
    min_j = j + 1

    turn = -1j

    cycles = 0

    obs_by_real = defaultdict(set)
    obs_by_imag = defaultdict(set)
    for p in obstacles:
        obs_by_real[p.real].add(p)
        obs_by_imag[p.imag].add(p)

    for new_obstacle in poss:
        pos = start_pos
        positions = set()
        direction = start_dir
        obs_by_imag[new_obstacle.imag].add(new_obstacle)
        obs_by_real[new_obstacle.real].add(new_obstacle)

        while max_i >= pos.real >= 0 >= pos.imag >= min_j:
            obs = get_next_obstacle(pos, direction, obs_by_real[pos.real], obs_by_imag[pos.imag])
            if (obs, direction) in positions:
                cycles += 1
                break
            positions.add((obs, direction))
            pos = obs - direction
            direction *= turn

        obs_by_imag[new_obstacle.imag].remove(new_obstacle)
        obs_by_real[new_obstacle.real].remove(new_obstacle)
    return cycles


def run():
    d, f = get_day_and_input(__file__)
    #     f = """....#.....
    # .........#
    # ..........
    # ..#.......
    # .......#..
    # ..........
    # .#..^.....
    # ........#.
    # #.........
    # ......#..."""
    log_start(d)
    part1 = part_1(f)
    log_part_1(len(part1))

    part2 = part_2(f, part1)
    log_part_2(part2)


if __name__ == "__main__":
    run()
