import csv
from collections import Counter
from operator import is_
from os import error
from pydoc import locate


def is_safe(report):
    '''
        Safe if:
        the levels are either all increasing or all decreasing.
        Any two adjacent levels differ by at least one and at most three.

        To Solve:
        Generate a list of deltas
        Check that either all deltas are increasing in the range or decreasing the range
    '''
    deltas = [a-b  for a,b in zip(report, report[1:])]
    return all(-3 <= n <= -1 for n in deltas) or all(1 <= n <= 3 for n in deltas)


def try_and_correct(report):
    """
        Check all possible removals to see if valid
    """
    return any(is_safe(report[:x] + report[x+1:]) for x in range(len(report)))

def part_1():
    with open("input.txt", "r") as f:
        data = [list(map(int, x.split(" "))) for x in f]
        safe_levels = [is_safe(x) for x in data]
    
    total_safe = sum(safe_levels)
    print(f"{total_safe=}")
    return total_safe


def part_2():
    with open("input.txt", "r") as f:
        data = [list(map(int, x.split(" "))) for x in f]
        safe_levels = [is_safe(x) for x in data]
        for idx, val in enumerate(data):
            if safe_levels[idx] == False:
                safe_levels[idx] = try_and_correct(val)


    total_safe = sum(safe_levels)
    print(f"{total_safe=}")

part_1()
part_2()
