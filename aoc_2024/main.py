import time

from loguru import logger

from aoc_2024 import day5, day6, day7, day8


def main():
    logger.info("Starting AOC 2023")
    timeit(day5.run)
    timeit(day6.run)
    timeit(day7.run)
    timeit(day8.run)


def timeit(fn):
    t = time.time()
    fn()
    logger.info(f"{fn.__module__} took {(time.time() - t) * 1000}ms")


if __name__ == "__main__":
    timeit(main)
