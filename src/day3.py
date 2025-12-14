import sys

ASCII_0 = ord('0')

def main():
    filename = sys.argv[1]

    with open(filename, "r") as f:
        sum_max = 0
        for bank in f:
            max_joltage = 0
            for i in range(len(bank)):
                for j in range(i+1, len(bank)):
                    joltage = 10 * (ord(bank[i]) - ASCII_0) + (ord(bank[j]) - ASCII_0)
                    if joltage > max_joltage:
                        max_joltage = joltage
            print(max_joltage)
            sum_max += max_joltage
        # Part 1
        print(sum_max)


if __name__ == "__main__":
    main()
