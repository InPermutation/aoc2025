import sys

def main():
    filename = sys.argv[1]

    beams = set()
    split_count = 0
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            nubeams = set()
            for ix in range(len(line)):
                ch = line[ix]
                if ch == 'S':
                    nubeams.add(ix)
                elif ch == '.':
                    if ix in beams:
                        nubeams.add(ix)
                elif ch == '^':
                    if ix in beams:
                        split_count += 1
                        nubeams.add(ix-1)
                        nubeams.add(ix+1)
            beams = nubeams
    print(split_count)

if __name__ == "__main__":
    main()
