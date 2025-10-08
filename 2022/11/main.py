import json


def monkey_objects(data):
    monkeys = dict()
    modulus = 1
    for monkey_data in data.split("\n\n"):
        current_monkey = ""
        for line in monkey_data.split("\n"):
            if line.startswith("Monkey"):
                current_monkey = int(line.split()[1].strip(":"))
                monkeys[current_monkey] = dict()
                continue

            if line.startswith("  Starting items:"):
                monkeys[current_monkey]["items"] = []
                items = line.split()[2:]
                for item in items:
                    monkeys[current_monkey]["items"].append(int(item.strip(",")))
                continue

            if line.startswith("  Operation:"):
                monkeys[current_monkey]["formula"] = line.split()[-3:]
                continue

            if line.startswith("  Test:"):
                monkeys[current_monkey]["test"] = int(line.split()[-1])
                modulus *= monkeys[current_monkey]["test"]
                continue

            if line.startswith("    If true:"):
                monkeys[current_monkey]["true"] = int(line.split()[-1])
                continue

            if line.startswith("    If false:"):
                monkeys[current_monkey]["false"] = int(line.split()[-1])
                continue

    return monkeys, modulus


def main(input):
    with open(f"{input}.txt") as f:
        data = f.read()
    monkeys, modulus = monkey_objects(data)
    print(json.dumps(monkeys, indent=4))
    operation = {
        "+": lambda x, y: x + y,
        "*": lambda x, y: x * y,
    }

    inspections = [0 for _ in range(len(monkeys))]
    round = 0
    while round < 10000 * len(monkeys):
        i = round % len(monkeys)
        op = operation[monkeys[i]["formula"][1]]

        for j in range(len(monkeys[i]["items"])):
            print("*" * 5 + f"Monkey {i}" + "*" * 5)
            item = monkeys[i]["items"].pop(0)
            print(f"Monkey {i} inspections item with worry level of {item}")
            modifier = item
            if monkeys[i]["formula"][-1] != "old":
                modifier = int(monkeys[i]["formula"][-1])

            inspections[i] += 1

            worry = op(item, modifier)
            print(f"Worry level is {monkeys[i]["formula"][1]} by {modifier} to {worry}")
            worry %= modulus
            target = monkeys[i]["false"]
            if worry % monkeys[i]["test"] == 0:
                target = monkeys[i]["true"]
                print(f"Current worry level is divisible by {monkeys[i]["test"]}")
            if worry % monkeys[i]["test"] != 0:
                print(f"Current worry level is not divisible by {monkeys[i]["test"]}")
            print(f"Item with worry level of {item} is thrown to monkey {target}")
            monkeys[target]["items"].append(worry)
        round += 1
        print("\n\n\n")
    print(f"Round {round // len(monkeys)}")
    for key, value in monkeys.items():
        print(monkeys[key]["items"])

    sorted_inspections = sorted(inspections)
    print(sorted_inspections[-1] * sorted_inspections[-2])


if __name__ == "__main__":
    main("data")
