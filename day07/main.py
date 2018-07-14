import re


def inside_brackets(num):
    if num == 0:
        return False
    if num % 2 == 0:
        return False
    else:
        return True


def search(address):
    flag, found = False, False
    for i, q in enumerate(address):
        x, y = 0, 4
        while y <= len(q):
            if q[x] == q[x + 3] and q[x + 1] == q[x + 2] and q[x] != q[x + 1]:
                if inside_brackets(i):
                    flag = True
                else:
                    found = True
            x += 1
            y += 1
    if not flag and found:
        return 1
    return 0


def search_ssl(address):
    aba, bab = [], []
    for i, q in enumerate(address):
        x, y = 0, 3
        while y <= len(q):
            if q[x] == q[x + 2] and q[x] != q[x + 1]:
                t = q[x] + q[x + 1] + q[x + 2]
                if inside_brackets(i):
                    bab.append(t)
                else:
                    aba.append(t)
            x += 1
            y += 1
    z = (1 for x in aba for y in bab if x[0] == y[1] and x[1] == y[0])
    if 1 in z:
        return 1
    return 0


def protocol_seven(puzzle, part):
    count = 0
    for line in puzzle:
        t = re.split('\\[|\\]', line)
        if part == 1:
            count += search(t)
        if part == 2:
            count += search_ssl(t)
    return count

if __name__ == '__main__':
    with open('input.txt', 'r') as text:
        print(protocol_seven(text, int(input('part: '))))
