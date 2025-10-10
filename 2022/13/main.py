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


def solve(data):
    pairs = data.split("\n\n")
    correct_indices = []

    for i, pair in enumerate(pairs, 1):
        left, right = pair.split("\n")
        left_packet = eval(left)
        right_packet = eval(right)

        if compare(left_packet, right_packet) == -1:
            correct_indices.append(i)

    return sum(correct_indices)


def main(input):
    with open(f"{input}.txt") as f:
        data = f.read().strip()
    sum = solve(data)
    print(sum)


if __name__ == "__main__":
    main("data")
