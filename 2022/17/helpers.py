import os

shapes = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(1, 0), (1, 1), (1, 2), (0, 1), (2, 1)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (0, 1), (1, 1)],
]


def getParsedData(input):
    with open(f"{input}.txt") as f:
        raw = f.read().strip()
    operations = []
    for dir in list(raw):
        if dir == ">":
            operations.append([1, 0])
        else:
            operations.append([-1, 0])

    # for i in range(len(operations)):
    #     print(f"{operations[i]}", {raw[i]})
    # print(raw)
    return operations, raw


def visualizeGrid(grid, raw, opp_idx):
    os.system("cls" if os.name == "nt" else "clear")
    if not grid:
        max_y = 0
    else:
        max_y = max(y for _, y in grid.keys()) + 8
    if max_y < 17:
        max_y = 17
    min_y = max(0, max_y - 20)  # Don't go below 0

    # Print from top to bottom (highest y first)
    for y in range(max_y, min_y - 1, -1):
        if y == 0:
            print("+" + "-" * 7 + "+")
            continue
        row = "|"  # Left wall
        for x in range(7):  # 0 to 6
            row += grid.get((x, y), ".")
        row += "|"  # Right wall
        print(f"{row}")

    print(raw)
    blank_row = ["." for x in range(len(list(raw)))]
    blank_row[opp_idx] = "*"
    blank_row = "".join(blank_row)
    print(blank_row)
