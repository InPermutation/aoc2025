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



if __name__ == "__main__":
    main()
