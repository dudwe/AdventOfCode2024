import csv
from collections import Counter
from pydoc import locate


def part_1():
    with open("input.txt", "r") as f:
        data = [list(map(int, x.split("   "))) for x in f]
        l1s, l2s = zip(*data)

    locations_ids_1 = sorted(list(l1s))
    locations_ids_2 = sorted(list(l2s))
    diffs = [
        abs(locations_ids_1[x] - locations_ids_2[x])
        for x in range(len(locations_ids_1))
    ]
    print(f"{sum(diffs)=}")
    return sum(diffs)


def part_2():
    """
    Calculate a total similarity score by adding up each number in the left
    list after multiplying it by the number of times that number appears in the right list.

    """
    with open("input.txt", "r") as f:
        data = [list(map(int, x.split("   "))) for x in f]
        locations_ids_1, locations_ids_2 = zip(*data)

    locations_ids_1 = list(locations_ids_1)
    locations_ids_2 = list(locations_ids_2)
    id_freqs = Counter(locations_ids_2)

    similarity = sum([id_freqs[x] * x for x in locations_ids_1])
    print(f"{similarity=}")
    return similarity

part_1()
part_2()
