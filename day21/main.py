def puzzle(unscramble):
    if unscramble:
        ins = reversed(instructions.read().splitlines())
    else:
        ins = instructions.read().splitlines()

    for line in ins:
        line = line.rstrip('\n')
        words = line.split(' ')
        print('{}, {}'.format(_input, line))
        if 'swap' in words:
            swap(words[2], words[5])
        elif 'based' in words:
            based(words[6], unscramble)
        elif 'reverse' in words:
            reverse(words[2], words[4])
        elif 'move' in words:
            move(words[2], words[5], unscramble)
        else:
            rotate(words[1], words[2], unscramble)


def swap(x, y):
    global _input
    if x.isdigit():
        x, y = map(int, (x, y))
    else:
        x, y = _input.index(x), _input.index(y)
    word = list(_input)
    word[x], word[y] = word[y], word[x]
    _input = ''.join(word)


def reverse(x, y):
    global _input
    x, y = map(int, (x, y))
    word = list(_input)
    word[x:y+1] = list(reversed(word[x:y+1]))
    _input = ''.join(word)


def move(x, y, r):
    global _input
    if r:
        x, y = map(int, (y, x))
    else:
        x, y = map(int, (x, y))
    word = list(_input)
    letter = word[x]
    del(word[x])
    word.insert(y, letter)
    _input = ''.join(word)


def rotate(direction, x, r):
    global _input
    if r:
        if direction == 'left':
            direction = 'right'
        else:
            direction = 'left'

    x = int(x)%len(_input)
    if direction == 'left':
        _input = _input[x:len(_input)] + _input[0:x]
    else:
        _input = _input[len(_input)-x:len(_input)] + _input[0:len(_input)-x]


def based(x, r):
    global _input
    pos = _input.index(x)
    if r:
        if pos % 2 == 0:
            pos = int(pos/2 + 5)
        elif pos % 2 == 1 or pos == 0:
            pos = int(pos/2 + 1)
        rotate('left', pos, False)

    elif pos >= 4:
        rotate('right', pos+2, False)
    else:
        rotate('right', pos+1, False)

with open('input.txt', 'r') as instructions:
    _input = 'fbgdceah'
    puzzle(True)
    print(_input)

