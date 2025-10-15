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


def find_uncovered_point(data_points, max_coords=20, min_coords=0):
    sensors_with_ranges = [
        (sensor, abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1]))
        for sensor, beacon in data_points
    ]

    for sensor, distance in sensors_with_ranges:
        sx, sy = sensor
        check_distance = distance + 1

        for dx in range(check_distance + 1):
            dy = check_distance - dx
            candidates = [
                (sx + dx, sy + dy),
                (sx - dx, sy + dy),
                (sx + dx, sy - dy),
                (sx - dx, sy - dy),
            ]

            for point in candidates:
                px, py = point

                if not (
                    min_coords <= px <= max_coords and min_coords <= py <= max_coords
                ):
                    continue

                if all(
                    abs(px - s[0]) + abs(py - s[1]) > d for s, d in sensors_with_ranges
                ):
                    return point
    return None


def main(input_file):
    with open(f"{input_file}.txt") as f:
        raw = f.read()

    max_y = 4000000 if input_file == "data" else 20
    data_points, _ = parse(raw)
    result = find_uncovered_point(data_points, max_y)
    print(f"Result: {(4000000 * result[0]) + result[1]}")


if __name__ == "__main__":
    main("data")
