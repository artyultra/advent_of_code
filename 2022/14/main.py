import os


def display_cave(cave):
    os.system("cls" if os.name == "nt" else "clear")

    # Parse coordinates
    coords = {}
    for key, value in cave.items():
        x, y = map(int, key.split(","))
        coords[(x, y)] = value

    # Find bounds
    if not coords:
        return

    xs = [x for x, y in coords.keys()]
    ys = [y for x, y in coords.keys()]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    # Print grid
    for y in range(min_y, max_y + 1):
        row = []
        for x in range(min_x, max_x + 1):
            if x == 500 and y == 0:
                row.append("+")  # Show the source
            else:
                row.append(coords.get((x, y), "."))
        print("".join(row))
    print()  # Empty line after grid


def normalize(raw):
    result = []
    for line in raw.split("\n"):
        coords = [
            [int(x), int(y)]
            for coord in line.split(" -> ")
            for x, y in [coord.split(",")]
        ]
        result.append(coords)
    return result


def get_line(a, b):
    x1, y1 = a
    x2, y2 = b

    if y1 == y2:
        start, end = min(x1, x2), max(x1, x2)
        return [(x, y1) for x in range(start, end + 1)]
    else:
        start, end = min(y1, y2), max(y1, y2)
        return [(x1, y) for y in range(start, end + 1)]


def place(normalized):
    max_y = 0
    max_x = 0
    cave = {}
    for rock_wall in normalized:
        start = []
        end = []
        for i in range(1, len(rock_wall)):
            start = rock_wall[i - 1]
            end = rock_wall[i]
            coords = get_line(start, end)
            for coord in coords:
                x, y = coord
                if y > max_y:
                    max_y = y
                if x > max_x:
                    max_x = x
                cave[f"{x},{y}"] = "#"

    return cave, [max_x, max_y]


def check_below(cave, x, y, floor):
    if y == floor:
        return True, [x, y - 1]
    if f"{x},{y}" not in cave:
        return False, [x, y]
    if f"{x - 1},{y}" not in cave:
        return False, [x - 1, y]
    if f"{x + 1},{y}" not in cave:
        return False, [x + 1, y]
    return True, [x, y - 1]


def sand_falling(cave, floor):
    resting = 0
    hole_clear = True
    while hole_clear:
        sx, sy = 500, 0
        is_falling = True
        while is_falling:
            check_x, check_y = sx, sy + 1
            is_resting, new_coords = check_below(cave, check_x, check_y, floor)
            nx, ny = new_coords
            if is_resting:
                if nx == 500 and ny == 0:
                    hole_clear = False
                cave[f"{nx},{ny}"] = "o"
                is_falling = False
                resting += 1
                break
            else:
                sx, sy = nx, ny

    return resting


def main(input):
    with open(f"{input}.txt") as f:
        raw = f.read().strip()
    normalized = normalize(raw)

    cave, max = place(normalized)
    resting = sand_falling(cave, max[1] + 2)

    print(f"resting: {resting}")


if __name__ == "__main__":
    main("data")
