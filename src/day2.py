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
                    for n in range(2, len(s) + 1):
                        uniq = seq_rep(s, n)
                        if len(uniq) == 1:
                            if n == 2:
                                invalid.add(i)
                            invalid2.add(i)

    # Part 1
    print(sum(invalid))
    # Part 2
    print(sum(invalid2))

# Divide a string into `n` constituent parts
def seq_rep(s: str, n: int) -> set[str]:
    if len(s) % n != 0:
        return set()

    w = len(s) // n
    start = 0
    res: set[str] = set()

    while start < len(s):
        res.add(s[start:start+w])
        start += w
    return res

if __name__ == "__main__":
    main()
