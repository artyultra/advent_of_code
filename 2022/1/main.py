def main():
    with open('data.txt') as f:
        data = f.read().split('\n')
    
    sample_dat = []
    current_group = []
    for item in data:
        if item == '':
            sample_dat.append(current_group)
            current_group = []
        else:
            current_group.append(item)

    totals = []
    for group in sample_dat:
        total = 0
        for str in group:
            num = int(str)
            total += num
        totals.append(total)

    totals.sort()
    top_three = totals[-3:]

    answer = 0
    for num in top_three:
        answer += num

    print(answer)

if __name__ == '__main__':
    main()
