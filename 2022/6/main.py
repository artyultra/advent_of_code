def partOne(input):
    with open(f"{input}.txt") as f:
        data = f.read().strip()

    letters = list(data)

    answer = 0
    for i in range(len(letters)):
        if i + 14 > len(letters):
            break
        check = letters[i : i + 14]
        if len(set(check)) == 14:
            answer = i + 14
            break

    print(answer)


if __name__ == "__main__":
    partOne("data")
