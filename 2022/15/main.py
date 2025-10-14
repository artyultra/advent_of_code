import re


def parse(raw):
    data_points = []
    beacons = set()

    for line in raw.strip().split("\n"):
        nums = list(map(int, re.findall(r"-?\d+", line)))
        sensor = (nums[0], nums[1])
        beacon = (nums[2], nums[3])
        data_points.append((sensor, beacon))
        beacons.add(beacon)

    return data_points, beacons


def get_x_range_at_y(sensor, distance, target_y):
    sx, sy = sensor
    dy = abs(target_y - sy)

    if dy > distance:
        return None

    remaining = distance - dy
    return (sx - remaining, sx + remaining)


def count_covered_positions(data_points, beacons, target_y):
    covered = set()

    for sensor, beacon in data_points:
        distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        x_range = get_x_range_at_y(sensor, distance, target_y)
        if x_range:
            for x in range(x_range[0], x_range[1] + 1):
                covered.add(x)

    beacons_xs_at_y = {bx for bx, by in beacons if by == target_y}
    return len(covered - beacons_xs_at_y)


def main(input_file):
    with open(f"{input_file}.txt") as f:
        raw = f.read()

    target_row = 2000000 if input_file == "data" else 10
    data_points, beacons = parse(raw)
    result = count_covered_positions(data_points, beacons, target_row)
    print(f"Result: {result}")


if __name__ == "__main__":
    main("sample")
