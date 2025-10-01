def partOne(input, priority):
    with open(f"{input}.txt") as f:
        data = f.read().split('\n')[:-1]

    total = 0
    for line in data:
        mid = len(line)//2
        left, right = line[:mid], line[mid:]
        print(left.split(), right.split())

        for char in left:
            if char in right:
                total += priorty[char]
                break
    print(total)

def partTwo(input, priority):
    with open(f"{input}.txt") as f:
        data = f.read().split('\n')[:-1]

    groups = []
    idx = 0
    while idx < len(data):
        new_group = []
        new_group.append(data[idx + 0])
        new_group.append(data[idx + 1])
        new_group.append(data[idx + 2])
        groups.append(new_group)
        idx += 3

    total = 0
    for group in groups:
        for char in group[0]:
            if char in group[1] and char in group[2]:
                total += priority[char]
                break
    print(total)

        


if __name__ == "__main__":
    priority = {
            "a" : 1,
            "b" : 2,
            "c" : 3,
            "d" : 4,
            "e" : 5,
            "f" : 6,
            "g" : 7,
            "h" : 8,
            "i" : 9,
            "j" : 10,
            "k" : 11,
            "l" : 12,
            "m" : 13,
            "n" : 14,
            "o" : 15,
            "p" : 16,
            "q" : 17,
            "r" : 18,
            "s" : 19,
            "t" : 20,
            "u" : 21,
            "v" : 22,
            "w" : 23,
            "x" : 24,
            "y" : 25,
            "z" : 26,
            "A" : 27,
            "B" : 28,
            "C" : 29,
            "D" : 30,
            "E" : 31,
            "F" : 32,
            "G" : 33,
            "H" : 34,
            "I" : 35,
            "J" : 36,
            "K" : 37,
            "L" : 38,
            "M" : 39,
            "N" : 40,
            "O" : 41,
            "P" : 42,
            "Q" : 43,
            "R" : 44,
            "S" : 45,
            "T" : 46,
            "U" : 47,
            "V" : 48,
            "W" : 49,
            "X" : 50,
            "Y" : 51,
            "Z" : 52,
            }
    # partOne("data", priority)
    partTwo("data", priority)
