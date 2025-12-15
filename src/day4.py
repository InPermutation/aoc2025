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

def count_accessible(d):
    accessible = 0
    for k, v in d.items():
        if v == '.':
            continue
        if is_accessible(k, d):
            accessible += 1
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
