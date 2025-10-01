def get_max_col(data):
    max_col = 0
    for line in data.split("\n"):
        if line.startswith(" 1"):
            break
        num_col = 0
        for char in line:
            if char == "[":
                num_col += 1

        if num_col > max_col:
            max_col = num_col

    return max_col


def get_columns(data, max_col):
    columns = [[] for _ in range(max_col)]

    for line in data.split("\n"):
        if line.startswith(" 1"):
            break

        char_index = 1
        for i in range(max_col):
            if line[char_index] != " ":
                columns[i].append(line[char_index])
            char_index += 4

    for i in range(len(columns)):
        columns[i] = list(reversed(columns[i]))
    return columns


def get_moves(data):
    moves = []
    for line in data.split("\n"):
        if line.startswith("move"):
            _, quantity, _, target, _, destination = line.split(" ")
            moves.append((int(quantity), int(target), int(destination)))
    return moves


def partOne(data):
    max_col = get_max_col(data)
    columns = get_columns(data, max_col)
    moves = get_moves(data)

    for move in moves:
        qty, src, dst = move
        columns[dst - 1] = columns[dst - 1] + columns[src - 1][qty * (-1) :]
        columns[src - 1] = columns[src - 1][: qty * (-1)]
    final = ""
    for col in columns:
        final += col[-1]
    print(final)
