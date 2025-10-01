import re


def parse(data):
    directory_sizes = {}
    curr_dir = ""
    for line in data.split("\n"):
        if line == "$ cd .." or line.startswith("$ ls") or line.startswith("dir"):
            print(f"skip: {line}")
            continue

        if line.startswith("$ cd"):
            curr_dir = line.split(" ")[2]
            print(f"cd: {line} | curr_dir: {curr_dir}")
            directory_sizes[curr_dir] = 0

        if re.match(r"[0-9]", line):
            size, name = line.split(" ")
            directory_sizes[curr_dir] += int(size)

    return directory_sizes


def main(input):
    with open(f"{input}.txt") as f:
        data = f.read()[:-1]

    directory_sizes = parse(data)

    sum = 0
    for dir, size in directory_sizes.items():
        print(f"{dir}: {size}")
        if dir == "/":
            continue
        if size <= 100000:
            sum += size
    print(sum)


if __name__ == "__main__":
    main("sample")
