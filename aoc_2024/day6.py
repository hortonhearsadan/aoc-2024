from loguru import logger

from aoc_2024.utils import get_day_and_input, by_line

OBSTACLE = "#"
GUARDS = ("^","V",">","<")

def part_1(data):
    obstacles = set()

    i = j =0
    pos = complex(0,0)

    for line in by_line(data):
        i=0
        for char in line:
            if char == OBSTACLE:
                obstacles.add(complex(i,j))
            elif char in GUARDS:
                pos = complex(i,j)
                match char:
                    case "^":
                        dir = 1j
                    case ">":
                        dir = 1
                    case "<":
                        dir = -1
                    case "V":
                        dir = -1j


            i+=1
        j-=1
    max_i = i-1
    min_j = j+1

    turn = -1j

    positions = {pos}
    while max_i >= pos.real >= 0 >= pos.imag >= min_j:
        positions.add(pos)
        new_pos = pos+dir
        if new_pos in obstacles:
            dir *= turn
        else:
            pos = new_pos
    return len(positions)

def part_2(data):
    obstacles = set()

    i = j =0
    start_pos = complex(0,0)

    for line in by_line(data):
        i=0
        for char in line:
            if char == OBSTACLE:
                obstacles.add(complex(i,j))
            elif char in GUARDS:
                start_pos = complex(i,j)
                match char:
                    case "^":
                        start_dir = 1j
                    case ">":
                        start_dir = 1
                    case "<":
                        start_dir = -1
                    case "V":
                        start_dir = -1j


            i+=1
        j-=1
    max_i = i-1
    min_j = j+1

    turn = -1j

    cycles = 0
    for r in range(max_i+1):
        for s in range(0,min_j-1,-1):
            pos = start_pos
            positions = set()
            dir = start_dir
            new_obstacle =complex(r,s)
            new_obstacles = obstacles | {new_obstacle}

            while max_i >= pos.real >= 0 >= pos.imag >= min_j:
                if (pos,dir) in positions:
                    cycles+=1
                    break
                positions.add((pos,dir))
                new_pos = pos+dir
                if new_pos in new_obstacles:
                    dir *= turn
                else:
                    pos = new_pos
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
    logger.info(f"Starting Day {d}")
    part1 = part_1(f)
    logger.info(f"Part 1: {part1}")

    part2 = part_2(f)
    logger.info(f"Part 2: {part2}")

if __name__ == '__main__':
    run()
