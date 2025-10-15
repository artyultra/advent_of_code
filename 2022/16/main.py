import re
from collections import deque
import time


def parse(raw):
    valves = {}
    important_valves = []
    pattern = r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)"
    lines = raw.strip().split("\n")
    for line in lines:
        m = re.match(pattern, line)
        if m:
            valve = m.group(1)
            flow = int(m.group(2))
            leads_str = m.group(3)
            leads = leads_str.split(", ")
            valves[valve] = {"rate": flow, "leads": leads}
            if flow > 0:
                important_valves.append(valve)
    return valves, important_valves


def shortest_path(valves, start, end):
    if start == end:
        return [start]

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        current, path = queue.popleft()

        for neighbour in valves[current]["leads"]:
            if neighbour == end:
                return path + [neighbour]

            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, path + [neighbour]))
    return []


def precompute_distances(valves, important_valves):
    distances = {}
    nodes = important_valves + ["AA"]
    for start in nodes:
        for end in nodes:
            if start != end:
                path = shortest_path(valves, start, end)
                distances[(start, end)] = len(path) - 1
    return distances


def max_pressure(valves, distances, current, remaining_valves, time_left, memo):
    if time_left <= 0 or not remaining_valves:
        return 0

    state = (current, frozenset(remaining_valves), time_left)
    if state in memo:
        return memo[state]

    best = 0

    for valve in remaining_valves:
        travel_time = distances[(current, valve)]
        open_time = 1
        total_time = travel_time + open_time

        if total_time <= time_left:
            remaining_time = time_left - total_time
            pressure = valves[valve]["rate"] * remaining_time

            new_remaining = [v for v in remaining_valves if v != valve]
            future_pressure = max_pressure(
                valves, distances, valve, new_remaining, remaining_time, memo
            )

            best = max(best, pressure + future_pressure)

    return best


def solve(valves, important_valves):
    distances = precompute_distances(valves, important_valves)
    best = 0
    n = len(important_valves)
    memo = {}

    print(f"Tryeing {1 << (n - 1)} splits...")

    for mask in range(1 << (n - 1)):
        if mask % 100 == 0:
            print(f"progress: {mask}/{1 << (n - 1)}")

        my_valves = []
        elephant_valves = []

        for i in range(n):
            if mask & (1 << i):
                my_valves.append(important_valves[i])
            else:
                elephant_valves.append(important_valves[i])

        my_pressure = max_pressure(valves, distances, "AA", my_valves, 26, memo)
        elephant_pressure = max_pressure(
            valves, distances, "AA", elephant_valves, 26, memo
        )
        total = my_pressure + elephant_pressure
        best = max(best, total)
    return best


def main(input):
    with open(f"{input}.txt") as f:
        raw = f.read()
    valves, important_valves = parse(raw)

    result = solve(valves, important_valves)

    print(result)


if __name__ == "__main__":
    main("data")
