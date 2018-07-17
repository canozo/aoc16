def solve(puzzle, hard_mode=False):
    pos = 0
    variables = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    if hard_mode:
        variables['c'] = 1

    while 0 <= pos < len(puzzle):
        instruction = puzzle[pos].rstrip('\n').split()
        if 'cpy' in instruction:
            cpy(variables, instruction[1], instruction[2])
            pos += 1
        elif 'inc' in instruction:
            inc(variables, instruction[1])
            pos += 1
        elif 'dec' in instruction:
            dec(variables, instruction[1])
            pos += 1
        elif 'jnz' in instruction:
            pos += jnz(variables, instruction[1], instruction[2])
    print(variables['a'])


def cpy(variables, x, y):
    if x.isdigit() or x[0] == '-':
        variables[y] = int(x)
    else:
        variables[y] = variables[x]


def inc(variables, x):
    variables[x] += 1


def dec(variables, x):
    variables[x] -= 1


def jnz(variables, x, y):
    if x == '0' or (x in variables and variables[x] == 0):
        return 1
    return int(y)


def main():
    with open('input.txt', 'r') as puzzle:
        solve(puzzle.readlines(), True)


if __name__ == '__main__':
    main()
