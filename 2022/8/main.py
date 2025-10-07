def create_graph(data):
    rows = data.split("\n")[:-1]
    grid_list = [list(c) for c in rows]
    graph = dict()
    for i in range(len(grid_list)):
        for j in range(len(grid_list[i])):
            height = grid_list[i][j]
            graph[f"{i},{j}"] = int(height)
    return graph, len(grid_list), len(grid_list[0])


def check_trees(graph, row_len, col_len):
    scenic_scores = []

    for i in range(row_len):
        for j in range(col_len):
            # print("*" * 20)
            # print(f"NEXT TREE: {i},{j}")
            # print("*" * 20)
            tree_height = graph[f"{i},{j}"]
            current_score = 1

            # check each direction
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dy, dx in directions:
                blocked = False
                y, x = i + dy, j + dx
                # print(current_score)

                # Walk until edge
                count = 1
                while 0 <= y < row_len and 0 <= x < col_len:
                    # print(f"count: {count}")
                    if graph[f"{y},{x}"] >= tree_height:
                        if count == 0:
                            break
                        blocked = True

                        current_score *= count
                        # print("ADDED TO CURRENT SCORE")
                        count = 0
                        break
                    y += dy
                    x += dx
                    count += 1
                if not blocked:
                    if count == 0:
                        continue
                    count -= 1
                    current_score *= count
                    # print("ADDED TOCURRENT SCORE")
                    count = 0

            scenic_scores.append(current_score)

    return scenic_scores


def main(input):
    with open(f"{input}.txt") as f:
        data = f.read()
    graph, row_len, col_len = create_graph(data)
    scores = check_trees(graph, row_len, col_len)

    print(max(scores))


if __name__ == "__main__":
    main("sample")
    main("data")
