def partOne(sample=False):
    if sample:
        with open('sample.txt') as f:
            data = f.read()
    else:
        with open('data.txt') as f:
            data = f.read()

    data = data.split('\n')[:-1]
    
    combos = {
            "A X": 4,
            "A Y": 8,
            "A Z": 3,
            "B X": 1,
            "B Y": 5,
            "B Z": 9,
            "C X": 7,
            "C Y": 2,
            "C Z": 6,
            }

    total = 0
    for pair in data:
        total += combos[pair]

    print(f'Part 1: {total}')

def partTwo(sample=False):
    if sample:
        with open('sample.txt') as f:
            data = f.read()
    else:
        with open('data.txt') as f:
            data = f.read()

    sample_dat = data.split('\n')[:-1]

    combos = {
            "A X": 3,
            "A Y": 4,
            "A Z": 8,
            "B X": 1,
            "B Y": 5,
            "B Z": 9,
            "C X": 2,
            "C Y": 6,
            "C Z": 7,
            }

    total = 0
    for round in sample_dat:
        total += combos[round]

    print(f'Part 2: {total}')


if __name__ == '__main__':
    partOne(True)
    partTwo(True)
