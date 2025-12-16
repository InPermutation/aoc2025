import sys

def main():
    filename = sys.argv[1]

    rows = []
    with open(filename, "r") as f:
        lines = [line.strip("\r\n") for line in f]
        rows = [row.split() for row in lines]
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

    # Part 2:
    width = len(lines[0])
    answers = [1 if v == '*' else 0 for v in rows[-1]]
    ixop = len(rows[0]) - 1
    nums = []

    for x in range(width - 1, -1, -1):
        num = 0
        isempty = True
        for y in range(len(lines) - 1):
            ch = lines[y][x]
            if ch != ' ':
                isempty = False
                num = num * 10 + int(ch)
        if isempty:
            if rows[-1][ixop] == '+':
                for n in nums:
                    answers[ixop] += n
            else:
                for n in nums:
                    answers[ixop] *= n
            nums = []
            ixop -= 1
        else:
            nums.append(num)
            num = 0
    if any(nums):
        if rows[-1][ixop] == '+':
            for n in nums:
                answers[ixop] += n
        else:
            for n in nums:
                answers[ixop] *= n

    print("Part 2", sum(answers))


if __name__ == "__main__":
    main()
