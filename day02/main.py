def bathroom(instruction, start, keypad):
    x, y = start
    answer = ''
    for line in instruction:
        for char in line:
            _x, _y = x, y
            if char == 'U':
                _y -= 1
            if char == 'D':
                _y += 1
            if char == 'L':
                _x -= 1
            if char == 'R':
                _x += 1

            if not keypad[_y][_x] == ' ':
                x, y = _x, _y
        answer += keypad[y][x]
    return answer

_KEYPAD_ONE = [
    '     ',
    ' 123 ',
    ' 456 ',
    ' 789 ',
    '     '
]

_KEYPAD_TWO = [
    '       ',
    '   1   ',
    '  234  ',
    ' 56789 ',
    '  ABC  ',
    '   D   ',
    '       '
]

_START_ONE = 2, 2
_START_TWO = 3, 1

if __name__ == '__main__':
    with open('input.txt', 'r') as text:
        print(bathroom(text, _START_ONE, _KEYPAD_ONE))
    with open('input.txt', 'r') as text:
        print(bathroom(text, _START_TWO, _KEYPAD_TWO))
