import heapq as hq
from collections import defaultdict, deque

from aoc_2024.utils import get_day_and_input, log_part_1, log_part_2, log_start


class Space:
    def __init__(self, start, end, id_="."):
        self.start = start
        self.end = end
        self.id = id_

    def __len__(self):
        return self.end - self.start

    def __repr__(self):
        return f"Space<{self.start},{self.end},{self.id}>"

    def __str__(self):
        return self.id * (self.end - self.start)

    def checksum(self):
        return sum(int(self.id) * i for i in range(self.start, self.end))

    def __lt__(self, other):
        return self.start < other.start


def part_1(data):
    freespace = []
    free = False
    i = 0
    idx = 0
    free_indices = deque()
    for d in data.strip():
        if free:
            block = "."
        else:
            block = str(i)
            i += 1

        for _ in range(int(d)):
            freespace.append(block)
            if free:
                free_indices.append(idx)

            idx += 1

        free = not free

    space = list(freespace)
    while free_indices:
        end = space.pop()
        if end == ".":
            free_indices.pop()
            continue
        i = free_indices.popleft()
        space[i] = end

    total = 0
    for i, s in enumerate(space):
        total += int(s) * i

    return total


def part_2(data):
    filespaces = []
    freespaces_by_len = defaultdict(list)

    free = False
    idx = 0
    file_id = 0
    for d in data.strip():
        next_idx = idx + int(d)
        if free:
            if d != "0":
                s = Space(idx, next_idx)
                freespaces_by_len[len(s)].append(s)
        else:
            filespaces.append(Space(idx, next_idx, id_=str(file_id)))
            file_id += 1
        idx = next_idx
        free = not free

    for v in freespaces_by_len.values():
        hq.heapify(v)

    for filespace in filespaces[::-1]:
        space = len(filespace)
        freespace = find_space(space, freespaces_by_len)
        if not freespace:
            continue
        if len(freespace) == 0:
            continue
        if filespace.start < freespace.start:
            continue
        if len(filespace) <= len(freespace):
            filespace.start = freespace.start
            filespace.end = freespace.start + space
            freespace.start += space
            hq.heappush(freespaces_by_len[len(freespace)], freespace)

    return sum(filespace.checksum() for filespace in filespaces)


def find_space(space, freespaces):
    spaces = []
    for i in range(space, max(freespaces.keys()) + 1):
        if freespaces[i]:
            spaces.append(freespaces[i][0])
    if not spaces:
        return None
    freespace = min(spaces)
    return hq.heappop(freespaces[len(freespace)])


def run():
    d, f = get_day_and_input(__file__)
    # f ="2333133121414131402" noqa: ERA001
    log_start(d)
    part1 = part_1(f)
    log_part_1(part1)

    part2 = part_2(f)
    log_part_2(part2)


if __name__ == "__main__":
    run()
