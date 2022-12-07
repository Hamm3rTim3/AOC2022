
def rangeToSet(x):
    begin, end = x.split('-')
    return set(range(int(begin), int(end) + 1))

def main():
    completesubset = 0
    intersections = 0
    with open('../inputs/day4.txt') as f:
        for line in f:
            temp = line.strip()
            a, b = temp.split(',')

            aset = rangeToSet(a)

            bset = rangeToSet(b)
            # is b subset of a?
            if aset.issubset(bset):
                completesubset += 1
            # is a a subset of b?
            elif bset.issubset(aset):
                completesubset += 1

            if aset & bset:
                intersections += 1
    print(f'First Question, total enclosures: {completesubset}')
    print(f'Second question, intersections: {intersections}')

if __name__ == '__main__':
    main()