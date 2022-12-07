
def testChars(data, index, length):
    test = data[index:index + length]
    return len(set(test)) == length

def main():
    datastarts = []
    messagestart = []
    with open('../inputs/day6.txt') as f:
        data = f.read()
        for i in range(0,len(data)):
            if testChars(data, i, 4):
                datastarts.append(i+4)
            if testChars(data, i, 14):
                messagestart.append(i+14)
    print(f'First Question: {datastarts[0]}')
    print(f'Second Question: {messagestart[0]}')
if __name__ == '__main__':
    main()