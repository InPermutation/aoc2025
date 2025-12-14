import sys


def main():
    filename = sys.argv[1]

    dial = 50

    is_zero = 0
    clicks_zero = 0
    with open(filename, "r") as f:
        for line in f:
            num = int(line[1:])
            while num != 0:
                match line[0]:
                    case 'L':
                        dial -= 1
                        if dial == 0:
                            clicks_zero += 1
                        if dial == -1:
                            dial = 99
                    case 'R':
                        dial += 1
                        if dial == 100:
                            clicks_zero += 1
                            dial = 0
                num -= 1
            if dial == 0:
                is_zero += 1
    # Part 1
    print(is_zero)
    # Part 2
    print(clicks_zero)


if __name__ == "__main__":
    main()
