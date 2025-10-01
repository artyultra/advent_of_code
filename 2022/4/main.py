def partOne(input):
    with open(f"{input}.txt") as f:
        data = f.read().split("\n")[:-1]

    for i in range(len(data)):
        data[i] = data[i].split(",")
        for j in range(len(data[i])):
            data[i][j] = data[i][j].split("-")


    count = 0
    for line in data:
        sectionOne, sectionTwo = line
        a, b = int(sectionOne[0]), int(sectionOne[1])
        y, z = int(sectionTwo[0]), int(sectionTwo[1])

        group1 = range(a, b + 1)
        group2 = range(y, z + 1)
        if a in group2 and b in group2:
            count += 1
        elif y in group1 and z in group1:
            count += 1
        else:
            pass

    if input == "sample":
        print(f'Part 1 Sample: {count}')
    else:
        print(f'Part 1: {count}')

def partTwo(input):
    with open(f"{input}.txt") as f:
        data = f.read().split("\n")[:-1]

    for i in range(len(data)):
        data[i] = data[i].split(",")
        for j in range(len(data[i])):
            data[i][j] = data[i][j].split("-")

    count = 0
    for line in data:
        sectionOne, sectionTwo = line
        a, b = int(sectionOne[0]), int(sectionOne[1])
        y, z = int(sectionTwo[0]), int(sectionTwo[1])

        if a <= y <= b or a <= z <= b:
            count += 1
        elif y <= a <= z or y <= b <= z:
            count += 1
        else:
            pass


    if input == "sample":
        print(f'Part 2 Sample: {count}')
    else:
        print(f'Part 2: {count}')


if __name__ == "__main__":
    partOne("data")
    partTwo("data")
