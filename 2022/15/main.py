import re


def parse(raw):
    lines = raw.split("\n")
    data_points = []
    beacons = set()
    for line in lines:
        x_matches = re.findall(r"x=(-?\d+)", line)
        y_matches = re.findall(r"y=(-?\d+)", line)
        sensor = (int(x_matches[0]), int(y_matches[0]))
        beacon = (int(x_matches[1]), int(y_matches[1]))
        data_points.append([sensor, beacon])
        beacons.add(beacon)
    return data_points, beacons


def find_covered_target_row(data_points, target_row=10):
    row_coords = set()
    for sensor, beacon in data_points:
        distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        min_max = get_x_range_at_y(sensor, distance, target_row)
        if min_max is None:
            continue

        for x in range(min_max[0], min_max[1] + 1):
            row_coords.add((x, target_row))

    return row_coords


def get_x_range_at_y(sensor, distance, target_row):
    sx, sy = sensor

    dy = abs(target_row - sy)

    if dy > distance:
        return None

    remaining = distance - dy

    min_x = sx - remaining
    max_x = sx + remaining

    return (min_x, max_x)


def main(input):
    with open(f"{input}.txt") as f:
        raw = f.read().strip()
    target_row = 10
    if input == "data":
        target_row = 2000000
    data_points, beacons = parse(raw)
    row_coords = find_covered_target_row(data_points, target_row)
    count = 0
    for coord in row_coords:
        if coord in beacons:
            continue
        count += 1
    print(count)


if __name__ == "__main__":
    main("data")
