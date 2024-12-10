from collections import defaultdict, deque

from aoc_2024.utils import get_day_and_input_by_line, log_part_1, log_part_2, log_start


def part_1_2(data):
    top_map = [list(map(int, s)) for s in data]
    y = len(data)
    x = len(data[0])
    starts = [(i, j) for i, row in enumerate(top_map) for j, c in enumerate(row) if c == 0]
    q = deque([(s, s) for s in starts])

    trails = 0
    trailheads = defaultdict(set)

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while q:
        node, s = q.popleft()
        node_val = top_map[node[0]][node[1]]
        for a, b in directions:
            i, j = (node[0] + a, node[1] + b)
            if not (0 <= i < x and 0 <= j < y):
                continue

            neigh_val = top_map[i][j]

            if neigh_val != node_val + 1:
                continue
            if neigh_val == 9:
                trails += 1
                trailheads[s].add((i, j))
                continue
            q.append(((i, j), s))

    return sum(len(t) for t in trailheads.values()), trails


def alt(data):
    # Bit slower but cooler

    topo_map = {}
    starts = []
    for i, row in enumerate(data):
        for j, num in enumerate(row):
            n = int(num)
            key = complex(j, i)
            if num == 0:
                starts.append(key)
            topo_map[key] = n

    directions = (1, -1, 1j, -1j)

    q = deque([(s, s) for s in starts])

    trailheads = defaultdict(set)
    trails = 0
    while q:
        node, start = q.popleft()
        node_val = topo_map.get(node)
        for d in directions:
            neighbour = node + d
            neigh_val = topo_map.get(neighbour)
            if neigh_val is None:
                continue
            if neigh_val - node_val != 1:
                continue

            if neigh_val == 9:
                trailheads[start].add(neighbour)
                trails += 1
                continue
            q.append((neighbour, start))

    return sum(len(t) for t in trailheads.values()), trails


def run():
    d, f = get_day_and_input_by_line(__file__)
    #     f="""89010123
    # 78121874
    # 87430965
    # 96549874
    # 45678903
    # 32019012
    # 01329801
    # 10456732""".splitlines()

    log_start(d)
    part1, part2 = part_1_2(f)
    log_part_1(part1)
    log_part_2(part2)


if __name__ == "__main__":
    run()
