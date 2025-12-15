import sys

def main():
    filename = sys.argv[1]

    fresh_ranges = []

    with open(filename, "r") as f:
        for row in f:
            if row.strip()=='':
                break
            lb, ub = map(int, row.split('-'))
            fresh_ranges.append(range(lb, ub+1))

        fresh_ingredients = 0
        for row in f:
            ingredient = int(row.strip())
            if any((ingredient in r) for r in fresh_ranges):
                fresh_ingredients += 1

        print("Part 1", fresh_ingredients)

        untouched = False
        while not untouched:
            untouched = True
            fresh_ranges = sorted(
                    (r for r in fresh_ranges if r is not None),
                    key=lambda r: r.start
            )
            for i in range(len(fresh_ranges) - 1):
                a, b = fresh_ranges[i], fresh_ranges[i+1]
                if a.stop > b.start:
                    fresh_ranges[i] = None
                    fresh_ranges[i+1] = range(a.start, max(a.stop, b.stop))
                    untouched = False

        print("Part 2", sum(len(r) for r in fresh_ranges))

if __name__ == "__main__":
    main()
