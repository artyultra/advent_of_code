import json


def move_up(root, path):
    end = root["/"]
    folders = path[1:].split("/")[:-1]
    if len(folders) <= 1:
        return end, "/"
    for folder in folders[:-1]:
        end = end[folder]
    new_path = f"/{"/".join(folders[:-1])}/"
    return end, new_path


def create_file_tree(data):
    root = {}
    current_dir = root
    path = ""
    for line in data.split("\n"):
        if line.startswith("$"):
            if line == "$ cd ..":
                new_dir, new_path = move_up(root, path)
                current_dir = new_dir
                path = new_path
            elif line.startswith("$ ls"):
                continue
            else:
                _, _, key = line.split(" ")
                current_dir[key] = {}
                current_dir = current_dir[key]
                if key == "/":
                    path = "/"
                else:
                    path = path + key + "/"
        elif line.startswith("dir"):
            continue
        else:
            size, name = line.split(" ")
            current_dir[name] = int(size)

    return root


def get_all_totals(node, totals_list):
    if totals_list is None:
        totals_list = []

    total = 0
    for key, value in node.items():
        if isinstance(value, dict):
            total += get_all_totals(value, totals_list)
        else:
            total += value

    totals_list.append(total)

    return total


def main(input):
    with open(f"{input}.txt") as f:
        data = f.read()[:-1]

    root_dir = create_file_tree(data)

    totals_list = []
    get_all_totals(root_dir, totals_list)
    totals_list.sort()

    root_filesize = max(totals_list)
    unused = 70000000 - root_filesize
    min_filesize = 30000000 - unused
    directories = []
    for t in totals_list:
        if t >= min_filesize:
            directories.append(t)

    print(f"Min filesize: {min_filesize}")
    print(f"Answer: {min(directories)}")


if __name__ == "__main__":
    main("data")
