def move(d, paths):
    directions = {
        "U": (0, 1),
        "D": (0, -1),
        "L": (-1, 0),
        "R": (1, 0),
    }
    start = paths[0][-1]
    x = start[0] + directions[d][0]
    y = start[1] + directions[d][1]
    paths[0].append([x, y])
    for i in range(1, len(paths)):
        head = paths[i - 1][-1]
        tail = paths[i][-1]
        shifted = node_to_move(head, tail)
        if shifted is None:
            return paths
        paths[i].append(shifted)

    return paths


def node_to_move(end_pos, start_pos):
    bx, by = end_pos
    ax, ay = start_pos
    surounding_cells = [
        [ax + 1, ay],
        [ax - 1, ay],
        [ax, ay + 1],
        [ax, ay - 1],
        [ax, ay],
        [ax + 1, ay + 1],
        [ax - 1, ay + 1],
        [ax + 1, ay - 1],
        [ax - 1, ay - 1],
    ]

    if [bx, by] not in surounding_cells:
        return min(
            surounding_cells, key=lambda cell: abs(cell[0] - bx) + abs(cell[1] - by)
        )
    return None


def main(input):
    with open(f"{input}.txt") as f:
        data = f.read()[:-1].split("\n")
    visited = dict()
    visited["0, 0"] = True
    knot_paths = [
        [[0, 0]],
        [[0, 0]],
        [[0, 0]],
        [[0, 0]],
        [[0, 0]],
        [[0, 0]],
        [[0, 0]],
        [[0, 0]],
        [[0, 0]],
        [[0, 0]],
    ]
    for line in data:
        d, num = line.split(" ")[0], int(line.split(" ")[1])
        count = 0
        while count < num:
            knot_paths = move(d, knot_paths)
            count += 1

    tail_positions = knot_paths[-1]
    my_set = set(tuple(sublist) for sublist in tail_positions)
    print(len(my_set))


if __name__ == "__main__":
    main("data")
