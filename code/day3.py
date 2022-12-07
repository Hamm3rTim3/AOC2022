import string

def FindSame(packs):
    if len(packs) != 3:
        return 'Uh-oh'
    a, b, c = packs
    return set(a) & set(b) & set(c)

allpri = []

with open('../inputs/day3.txt') as f:
    for pack in f:
        pack = pack.strip()
        middle = int(len(pack)/2)
        comp1 = set(pack[:middle])
        comp2 = set(pack[middle:])
        same = comp1.intersection(comp2)
        allpri.append(string.ascii_letters.index(same.pop()) + 1)



print(f'Sum answer 1: {sum(allpri)}')

groups = {
    0: {
        'packs': [],
        'item': '',
        'priority': 0
    }
}

with open('../inputs/day3.txt') as f:
    count = 0
    member = 0

    for pack in f:
        member += 1
        pack = pack.strip()
        groups[count]['packs'].append(pack)

        if member == 3:
            same = FindSame(groups[count]['packs'])
            same = same.pop()
            groups[count]['priority'] = string.ascii_letters.index(same) + 1
            groups[count]['item'] = same
            count += 1
            member = 0
            groups[count] =  {
                'packs': [],
                'item': '',
                'priority': 0
            }

total = sum([group['priority'] for group in groups.values()])

print(f'Answer 2: {total}')
