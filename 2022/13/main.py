from itertools import product
import json
from math import prod


def print_data(data):
    for i in range(len(data)):
        if i < 10:
            print(f" {i}: {data[i]}")
            continue
        print(f"{i}: {data[i]}")


def compare(left, right):
    # Both integers
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0

    # Both lists
    if isinstance(left, list) and isinstance(right, list):
        for i in range(min(len(left), len(right))):
            result = compare(left[i], right[i])
            if result != 0:
                return result

        # All elements compare equally, check lengths
        if len(left) < len(right):
            return -1
        elif len(left) > len(right):
            return 1
        else:
            return 0

    # Mixed types (list and int)
    if isinstance(left, int):
        return compare([left], right)
    else:
        return compare(left, [right])


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if compare(arr[j], arr[j + 1]) == 1:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def solve(sorted_arr):
    indices = []
    for i in range(len(sorted_arr)):
        if str(sorted_arr[i]) == "[[2]]" or str(sorted_arr[i]) == "[[6]]":
            indices.append(i + 1)

    return prod(indices)


def main(input):
    with open(f"{input}.txt") as f:
        raw = f.read().strip()
        split_raw = raw.split("\n")
        processed = []
        for i in range(len(split_raw)):
            if split_raw[i] == "":
                continue
            processed.append(eval(split_raw[i]))

    # print_data(processed)
    sorted_data = bubble_sort(processed)
    print(solve(sorted_data))


if __name__ == "__main__":
    main("data")
