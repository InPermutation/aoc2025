import sys


def main():
    filename = sys.argv[1]

    invalid = 0
    invalid2 = 0
    with open(filename, "r") as f:
        for line in f:
            for bounds in line.split(','):
                lbound, rbound = map(int, bounds.split('-'))

                # range is exclusive of upper bound, so add 1
                r = range(lbound, rbound + 1)
                for i in r:
                    s = str(i)
                    ls = len(s)
                    for n in range(2, ls + 1):
                        if (ls % n) != 0:
                            continue

                        w = ls // n
                        start = w
                        orig = s[0:w]
                        while start < ls:
                            if orig != s[start:start+w]:
                                break
                            start += w
                        else:
                            if n == 2:
                                invalid += i
                            invalid2 += i
                            continue

    # Part 1
    print(invalid)
    # Part 2
    print(invalid2)

if __name__ == "__main__":
    main()
