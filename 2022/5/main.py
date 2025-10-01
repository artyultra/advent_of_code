from part_one import partOne


def main(input):
    with open(f"{input}.txt") as f:
        data = f.read()

    partOne(data)


if __name__ == "__main__":
    main("data")
