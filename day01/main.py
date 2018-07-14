def taxi(directions):
    pos = [0,  0]
    ins = [0, -1]
    for seq in directions:
        turn = seq[0]
        walk = int(seq[1:])
        ins[turn == 'L'] *= -1
        ins = ins[::-1]
        pos[0] += ins[0] * walk
        pos[1] += ins[1] * walk
    return pos


def crazy_taxi(directions):
    pos = [0, 0]
    ins = [0, -1]
    for seq in directions:
        turn = seq[0]
        walk = int(seq[1:])
        ins[turn == 'L'] *= -1
        ins = ins[::-1]
        for t in range(1, walk + 1):
            yield(
                pos[0] + ins[0] * t,
                pos[1] + ins[1] * t,
            )
        pos[0] += ins[0] * walk
        pos[1] += ins[1] * walk
    return pos


def generator(directions):
    backlog = {(0, 0)}
    for moves in crazy_taxi(directions):
        if moves in backlog:
            return moves
        backlog.add(moves)

exam = 'R8, R4, R4, R8'

if __name__ == '__main__':
    with open('input.txt', 'r') as text:
        _input = text.read().split(', ')
        print(sum(map(abs, generator(_input))))
