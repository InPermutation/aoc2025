import sys


def main():
    filename = sys.argv[1]

    invalid = set()
    invalid2 = set()
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
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
                                invalid.add(i)
                            invalid2.add(i)

    # Part 1
    print(sum(invalid))
    # Part 2
    print(sum(invalid2))

if __name__ == "__main__":
    main()
