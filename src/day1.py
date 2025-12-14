import sys


def main():
    filename = sys.argv[1]

    dial = 50

    # Part 1
    is_zero = 0
    with open(filename, "r") as f:
        for line in f:
            print("LINE:", line)
            num = int(line[1:])
            if line[0] == "R":
                dial += num
            else:
                dial -= num
            dial = dial % 100
            if dial == 0:
                is_zero += 1
    print(is_zero)


if __name__ == "__main__":
    main()
