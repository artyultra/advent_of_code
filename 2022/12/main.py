def create_matrix(data: list[str]):
    height = len(data)
    width = len(data[0])
    matrix = [[0 for _ in range(width)] for _ in range(height)]
    start = []
    end = []
    for i in range(height):
        for j in range(width):
            char = data[i][j]
            if char == "S":
                start = [i, j]
                matrix[i][j] = ord("a") - ord("a") + 1
                continue

            if char == "E":
                end = [i, j]
                matrix[i][j] = ord("z") - ord("a") + 1
                continue

            val = ord(char) - ord("a") + 1
            matrix[i][j] = val

    return matrix, start, end


def get_possible_moves(matrix, current, visited):
    allowed = []
    directions = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1],
    ]
    for direction in directions:
        y, x = current
        current_height = matrix[y][x]
        dy, dx = y + direction[0], x + direction[1]
        if 0 <= dy < len(matrix) and 0 <= dx < len(matrix[0]):
            if (dy, dx) in visited:
                continue

            dir_height = matrix[dy][dx]
            if dir_height - current_height > 1:
                continue

            allowed.append([dy, dx])

    return allowed


def find_path(matrix, start, end):
    visited = set()
    queue = [(start, [start])]
    visited.add(tuple(start))

    while queue:
        current, path = queue.pop(0)

        if current == end:
            return len(path) - 1

        possible_moves = get_possible_moves(matrix, current, visited)

        for move in possible_moves:
            move_tup = tuple(move)
            if move_tup not in visited:
                visited.add(move_tup)
                queue.append((move, path + [move]))

    return None


def main(input="sample"):
    with open(f"{input}.txt") as f:
        data = f.read().split("\n")[:-1]

    matrix, start, end = create_matrix(data)

    paths = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                path_opt = find_path(matrix, [i, j], end)
                if path_opt:
                    paths.append(path_opt)

    print(min(paths))


if __name__ == "__main__":
    main("data")
