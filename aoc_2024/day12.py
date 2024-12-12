from collections import defaultdict

import networkx as nx
from networkx import Graph

from aoc_2024.utils import get_day_and_input_by_line, log_part_1, log_part_2, log_start

DIRECTIONS = (1, -1, 1j, -1j)


def adjacent(node1, node2):
    return abs(node1[0] - node2[0]) == 1 and abs(node1[1] - node2[1]) == 1


def part1_2(data):
    garden = defaultdict(set)
    for i, row in enumerate(data):
        for j, plot in enumerate(row):
            garden[plot].add(complex(j, -i))

    total_cost = 0
    discount_cost = 0
    outs = defaultdict(list)
    for _plot, locations in garden.items():
        graphs = Graph()
        for location in locations:
            graphs.add_node(location)
            for direction in DIRECTIONS:
                neighbour = location + direction
                if neighbour in locations:
                    graphs.add_edge(location, neighbour)
                else:
                    outs[location].append(neighbour)

        subsets = nx.connected_components(graphs)

        for sub in subsets:
            perim_sub = [(n, o) for n in sub for o in outs[n]]
            area = len(sub)
            perim = len(perim_sub)
            sides = perim
            for i, node in enumerate(perim_sub):
                for node2 in perim_sub[i + 1 :]:
                    if node == node2:
                        continue
                    if adjacent(node, node2):
                        sides -= 1
            disc_cost = area * sides
            full_cost = area * perim
            total_cost += full_cost
            discount_cost += disc_cost

    return total_cost, discount_cost


def run():
    d, f = get_day_and_input_by_line(__file__)
    #     f="""RRRRIICCFF
    # RRRRIICCCF
    # VVRRRCCFFF
    # VVRCCCJFFF
    # VVVVCJJCFE
    # VVIVCCJJEE
    # VVIIICJJEE
    # MIIIIIJJEE
    # MIIISIJEEE
    # MMMISSJEEE""".splitlines()

    log_start(d)
    part1, part2 = part1_2(f)
    log_part_1(part1)

    log_part_2(part2)


if __name__ == "__main__":
    run()
