d = open('input.txt')
database = d.read().splitlines()
d.close()
nodes = []

for i in range(2, len(database)):
    cord, size, used, avail, perc = database[i].strip().split()

    xi = cord.index('x')
    yi = cord.index('y')

    x = int(cord[xi + 1:yi - 1])
    y = int(cord[yi + 1:])

    size, used, avail, perc = (int(x[:-1]) for x in (size, used, avail, perc))

    nodes.append((x, y, size, used, avail))

count = 0

for i in range(len(nodes)):
    for j in range(len(nodes)):
        if i == j:
            continue

        a = nodes[i]
        b = nodes[j]
        if a[3] != 0 and a[3] <= b[-1]:
            count += 1

print(count)

