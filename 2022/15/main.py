import re


def parse(raw):
    lines = raw.split("\n")
    data_points = []
    for line in lines:
        x_matches = re.findall(r"x=(-?\d+)", line)
        y_matches = re.findall(r"y=(-?\d+)", line)
        sensor = (int(x_matches[0]), int(y_matches[0]))
        beacon = (int(x_matches[1]), int(y_matches[1]))
        data_points.append([sensor, beacon])
    return data_points


def get_rows(grid_dict):
    coords = list(grid_dict.keys())
    min_x = min(x for x, y in coords)
    max_x = max(x for x, y in coords)
    min_y = min(y for x, y in coords)
    max_y = max(y for x, y in coords)

    # Create 2D list
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    grid = [["." for _ in range(width)] for _ in range(height)]

    # Populate from dictionary
    for (x, y), value in grid_dict.items():
        grid[y - min_y][x - min_x] = value

    return grid, min_y


def get_coordinates_in_range(center, range_distance):
    x, y = center
    coordinates = []

    for dx in range(-range_distance, range_distance + 1):
        # For each horizontal offset, calculate vertical range
        remaining = range_distance - abs(dx)
        for dy in range(-remaining, remaining + 1):
            coordinates.append((x + dx, y + dy))

    return coordinates


def populate(data_points):
    grid = dict()
    for sensor, beacon in data_points:
        grid[sensor] = "S"
        grid[beacon] = "B"
        distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        for coord in get_coordinates_in_range(sensor, distance):
            if coord in grid:
                continue
            grid[coord] = "#"

    return grid, get_rows(grid)


def main(input):
    with open(f"{input}.txt") as f:
        raw = f.read().strip()
    data_points = parse(raw)
    grid, visual_return = populate(data_points)

    sum = 0
    visual_grid, min_y = visual_return
    for val in visual_grid[10 - min_y]:
        if val == "#":
            sum += 1

    print(sum)


if __name__ == "__main__":
    main("data")
