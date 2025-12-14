import sys


def main():
    filename = sys.argv[1]

    invalid = set()
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            for bounds in line.split(','):
                print(bounds)

                lbound, rbound = map(int, bounds.split('-'))

                # range is exclusive of upper bound, so add 1
                r = range(lbound, rbound + 1)
                for i in r:
                    s = str(i)
                    if len(s) % 2 != 0:
                        continue
                    hlen = len(s) // 2
                    l, r = s[:hlen], s[hlen:]
                    if l == r:
                        invalid.add(i)

    # Part 1
    print(sum(invalid))


if __name__ == "__main__":
    main()
