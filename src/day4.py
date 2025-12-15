import sys

def main():
    filename = sys.argv[1]

    d = {}
    with open(filename, "r") as f:
        y = 0
        for row in f:
            row = row.strip()
            x = 0
            for val in row:
                d[(x, y)] = val
                x += 1
            y += 1

    accessible = count_accessible(d)

    print("Part 1", accessible)

    total_removed = 0
    while True:
        remove = accessible_rolls(d)
        if len(remove) == 0:
            break

        for v in remove:
            d[v] = '.'
        total_removed += len(remove)

    print("Part 2", total_removed)

def count_accessible(d):
    return len(accessible_rolls(d))

def accessible_rolls(d):
    accessible = []
    for k, v in d.items():
        if v == '.':
            continue
        if is_accessible(k, d):
            accessible.append(k)
    return accessible

def is_accessible(k, d):
        occupied_neighbors = 0
        for neighbor in neighbors(k):
            if d.get(neighbor) == '@':
                occupied_neighbors += 1
        return occupied_neighbors < 4

def neighbors(k):
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if x == 0 and y == 0:
                continue
            yield (k[0]+x, k[1]+y)



if __name__ == "__main__":
    main()
