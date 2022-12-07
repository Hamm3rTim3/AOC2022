strategy = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y',
    'X': 'C',
    'Y': 'A',
    'Z': 'B'
}

pts = {
    'X': 1,
    'Y': 2,
    'Z': 3,
    'A': 1,
    'B': 2,
    'C': 3
}

total = 0
inputs = []
with open('../inputs/day2.txt') as f:
    for line in f:
        if line == '\n':
            continue
        opp, me = line.split()
        inputs.append((opp, me))
        #loss
        if strategy[opp] == me:
            total += pts[me]
        #win
        elif strategy[me] == opp:
            total += 6 + pts[me]
        #draw
        else:
            total += 3 + pts[me]

print(f'Total Score Part 1: {total}')
total = 0
for opp, outcome in inputs:
    #lose
    if outcome == 'X':
        me = strategy[opp]
    #draw
    elif outcome == 'Y':
        me = opp
        total += 3
    #win
    else:
        me = None
        for x in strategy:
            if opp == strategy[x]:
                me = x
                break
        total += 6

    total += pts[me]

print(f'New Score Part 2: {total}')
