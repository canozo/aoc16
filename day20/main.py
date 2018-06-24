def puzzle():
    blocked = []
    for line in text:
        r_from, r_to = map(int, line.split('-'))
        blocked.append((r_from, r_to))

    blocked.sort(key=lambda x: x[0])
    prev = blocked[0]
    allowed = 0

    for i in range(1, len(blocked)):
        curr = blocked[i]
        if prev[1] > curr[0] and prev[1] > curr[1]:
            continue
        elif prev[1] > curr[0]:
            prev = (prev[0], curr[1])
            continue

        print(prev, curr)
        allowed += curr[0] - prev[1] - 1
        prev = curr
    return allowed

with open('input.txt', 'r') as text:
    print(puzzle())

