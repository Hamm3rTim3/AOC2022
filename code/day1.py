elves = []

with open('../inputs/day1.txt') as f:
    total = 0
    for line in f:
        if line == '\n':
            elves.append(total)
            total = 0
        else:
            total += int(line.replace('\n', ''))


print(f'Output Answer 1: {max(elves)}')
elves.sort()
print(f'Output Answer 2: {sum(elves[-3:])}')
