import networkx as nx

from aoc_2024.utils import by_line, get_day_and_input, log_part_1, log_part_2, log_start


def part_1_2(data):
    graph = nx.DiGraph()
    paths = []
    for line in by_line(data):
        if "|" in line:
            u, v = line.split("|")
            graph.add_edge(int(u), int(v))

        elif "," in line:
            paths.append([int(s.strip()) for s in line.split(",")])

    count_1 = 0
    count_2 = 0
    for path in paths:
        sub = graph.subgraph(path)
        if nx.is_path(sub, path):
            count_1 += path[int((len(path)) / 2)]

        else:
            try:
                p = list(nx.topological_sort(sub))
                count_2 += p[int((len(p)) / 2)]
            except:  # noqa: S112,E722
                continue

    return count_1, count_2


def run():
    d, f = get_day_and_input(__file__)

    log_start(d)
    part1, part2 = part_1_2(f)
    log_part_1(part1)
    log_part_2(part2)


if __name__ == "__main__":
    run()
