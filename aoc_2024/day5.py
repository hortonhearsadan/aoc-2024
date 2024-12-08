from itertools import combinations, permutations

import networkx as nx
from loguru import logger

from aoc_2024.utils import get_day_and_input, by_line


def part_1(data):
    graph = nx.DiGraph()
    paths = []
    for line in by_line(data):
        if "|" in line:
            u,v = line.split("|")
            graph.add_edge(int(u),int(v))

        elif "," in line:
            paths.append([int(s.strip()) for s in line.split(",")])

    count = 0

    for path in paths:

        if nx.is_path(graph,path):
            count += path[int((len(path)) / 2)]

    return count

def part_2(data):
    graph = nx.DiGraph()
    paths = []
    for line in by_line(data):
        if "|" in line:
            u, v = line.split("|")
            graph.add_edge(int(u), int(v))

        elif "," in line:
            paths.append([int(s.strip()) for s in line.split(",")])

    count = 0
    for path in paths:
        sub = graph.subgraph(path)
        if not nx.is_path(sub,path):
            try:
                p = list(nx.topological_sort(sub))
                count += p[int((len(p)) / 2)]
            except:
                continue

    return count

def run():
    d, f = get_day_and_input(__file__)

    logger.info(f"Starting Day {d}")
    part1 = part_1(f)
    logger.info(f"Part 1: {part1}")

    part2 = part_2(f)
    logger.info(f"Part 2: {part2}")


if __name__ == '__main__':
    run()