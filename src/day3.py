import sys

UP_TO = 12

def main():
    filename = sys.argv[1]

    with open(filename, "r") as f:
        sum_max = 0
        sum_max2 = 0
        for bank in f:
            bank = bank.strip()

            last = [int(i) for i in bank]
            # for the first battery, either it is selected or not
            for ix in range(len(bank) - 2, -1, -1):
                last[ix] = max(last[ix+1], last[ix])

            for digit_count in range(2, UP_TO + 1):
                curr = [int(i) for i in bank]
                # upper bound = [-digit_count]:
                # cannot physically select more batteries than that
                ubound = len(curr) - digit_count
                for ix in range(ubound, -1, -1):
                    curr[ix] = max(
                            curr[ix + 1],
                            int(bank[ix]) * (10**(digit_count-1)) + last[ix + 1])
                last = curr
                if digit_count == 2:
                    max_joltage = max(curr)
                elif digit_count == 12:
                    max_joltage2 = max(curr)
            sum_max += max_joltage
            sum_max2 += max_joltage2

        # Part 1
        print(sum_max)
        # Part 2
        print(sum_max2)

if __name__ == "__main__":
    main()
