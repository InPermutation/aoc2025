import sys

def main():
    filename = sys.argv[1]

    rows = []
    with open(filename, "r") as f:
        rows = [row.split() for row in f]
    width = len(rows[0])

    # start with multiplicative/additive identities:
    answers = [1 if v == '*' else 0 for v in rows[-1]]

    for col in range(width):
        for row in rows[:-1]:
            if rows[-1][col] == '*':
                answers[col] *= int(row[col])
            else:
                answers[col] += int(row[col])

    print("Part 1", sum(answers))


if __name__ == "__main__":
    main()
