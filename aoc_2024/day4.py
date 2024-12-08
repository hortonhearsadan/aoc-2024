from aoc_2024.utils import get_day_and_input_by_line, log_part_1, log_part_2, log_start


def part_1(data):
    count = 0
    for i, row in enumerate(data):
        for j, char in enumerate(row):
            if 0 < i < len(data) - 2:
                vsub = data[i - 1][j] + char + data[i + 1][j] + data[i + 2][j]
                if has_xmas(vsub):
                    count += 1

            if 0 < j < len(row) - 2:
                hsub = row[j - 1 : j + 3]
                if has_xmas(hsub):
                    count += 1

                if 0 < i < len(data) - 2:
                    ldsub = data[i - 1][j - 1] + char + data[i + 1][j + 1] + data[i + 2][j + 2]
                    if has_xmas(ldsub):
                        count += 1

                if 1 < i < len(data) - 1:
                    odsub = data[i + 1][j - 1] + char + data[i - 1][j + 1] + data[i - 2][j + 2]
                    if has_xmas(odsub):
                        count += 1
    return count


def part_2(data):
    count = 0
    for i, row in enumerate(data):
        for j, char in enumerate(row):
            if 0 < i < len(data) - 1 and 0 < j < len(row) - 1:
                ldsub = data[i - 1][j - 1] + char + data[i + 1][j + 1]
                odsub = data[i + 1][j - 1] + char + data[i - 1][j + 1]
                if has_cross_mas(ldsub, odsub):
                    count += 1
    return count


def has_xmas(s):
    return "XMAS" in s or "SAMX" in s


def has_mas(s):
    return "MAS" in s or "SAM" in s


def has_cross_mas(s, t):
    return has_mas(s) and has_mas(t)


def run():
    d, f = get_day_and_input_by_line(__file__)
    #     f = '''MMMSXXMASM
    # MSAMXMSMSA
    # AMXSXMAAMM
    # MSAMASMSMX
    # XMASAMXAMM
    # XXAMMXXAMA
    # SMSMSASXSS
    # SAXAMASAAA
    # MAMMMXMMMM
    # MXMXAXMASX'''.split("\n")

    log_start(d)
    part1 = part_1(f)
    log_part_1(part1)

    part2 = part_2(f)
    log_part_2(part2)


if __name__ == "__main__":
    run()
