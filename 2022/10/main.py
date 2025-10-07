def create_grid():
    length = 40
    height = 6
    return [[" " for _ in range(length)] for _ in range(height)]


def main(input):
    with open(f"{input}.txt") as f:
        raw = f.read()
    lines = raw.split("\n")
    grid = create_grid()
    sprite_pos = [0, 1, 2]
    cycle = 0
    add = 0
    for line in lines[:-1]:
        # print(f"{cycle} - {sprite_pos[0]} {sprite_pos[1]} {sprite_pos[2]}")
        count = 1
        if line.startswith("addx"):
            _, val = line.split(" ")
            add = int(val)
            count = 2
        if line == "noop":
            add = 0
        i = 0
        while i < count:
            x = cycle % 40
            y = cycle // 40
            if x in sprite_pos:
                grid[y][x] = "#"
            if x not in sprite_pos:
                grid[y][x] = "."
            # print("".join(grid[y]))
            cycle += 1
            i += 1
        sprite_pos = [x + add for x in sprite_pos]

    for row in grid:
        print("".join(row))


if __name__ == "__main__":
    main("data")
