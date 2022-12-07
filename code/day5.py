
def main():
    containers = []
    newcont = {}
    rules = []
    with open('../inputs/day5.txt') as f:
        populated = False
        for line in f:
            line = line.strip('\n')
            if not line:
                populated = True
                #transpose to make our lives easier
                transposed = list(zip(*containers))
                for row in transposed:
                    row = list(row)
                    row.reverse()
                    srow = ''.join(row)
                    if srow[0] != ' ':
                        srow = srow.strip()
                        newcont[row[0]] = list(srow[1:])
                containers = {i:newcont[i].copy() for i in newcont}
            elif line and populated:
                move, cfrom, cto = line.split(' ')[1::2]
                rules.append((move, cfrom, cto))
                for i in range(0,int(move)):
                    newcont[cto].append(newcont[cfrom].pop())
            if not populated:
                containers.append(list(line))

    out1 = ''.join([item[-1] for item in newcont.values()])
    print(f'First Question: {out1}')

    for move, f, t in rules:
        containers[t] += containers[f][int(move) * -1:]
        containers[f] = containers[f][:int(move) * -1]
    out2 = ''.join([item[-1] for item in containers.values()])
    print(f'Second Question: {out2}')
if __name__ == '__main__':
    main()