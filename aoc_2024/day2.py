from aoc_2024.utils import get_day_and_input_by_line, log_part_1, log_part_2, log_start


def is_safe(level):
    asc = level[0] < level[1]
    for x, y in zip(level, level[1:]):
        if x == y:
            return False
        if (x < y) != asc:
            return False
        if abs(x - y) > 3:
            return False
    return True


def part_1(data):
    count = 0
    for d in data:
        level = list(map(int, d.split(" ")))
        if is_safe(level):
            count += 1

    return count


def part_2(data):
    count = 0
    for d in data:
        level = list(map(int, d.split(" ")))
        if is_safe(level):
            count += 1
        else:
            for i in range(len(level)):
                new_level = level[:]
                del new_level[i]
                if is_safe(new_level):
                    count += 1
                    break
    return count


def run():
    d, f = get_day_and_input_by_line(__file__)
    log_start(d)
    part1 = part_1(f)
    log_part_1(part1)

    part2 = part_2(f)
    log_part_2(part2)


if __name__ == "__main__":
    run()
