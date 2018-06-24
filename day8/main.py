def rect(a, b, screen):
    return [['#' if x < a and y < b else screen[y][x] for x in range(50)] for y in range(6)]


def rotate_row(a, b, screen):
    screen[a] = screen[a][-b:] + screen[a][:-b]
    return screen


def rotate_column(a, b, screen):
    original = [screen[x][a] for x in range(6)]
    original = original[-b:] + original[:-b]
    return [[original[y] if a == x else screen[y][x] for x in range(50)] for y in range(6)]


def control_room(instructions, screen):
    for line in instructions:
        line = line.split()
        if 'rect' in line:
            a, b = (int(j) for j in line[1].split('x'))
            screen = rect(a, b, screen)
        if 'rotate' and 'row' in line:
            a, b = int(line[2].split('=')[1]), int(line[4])
            screen = rotate_row(a, b, screen)
        if 'rotate' and 'column' in line:
            a, b = int(line[2].split('=')[1]), int(line[4])
            screen = rotate_column(a, b, screen)
    print_screen(screen)
    return [1 for line in screen for char in line if char == '#'].count(1)


def print_screen(screen):
    for line in screen:
        for char in line:
            print(char, end='')
        print('')

_SCREEN = [['.' for y in range(50)] for x in range(6)]

if __name__ == '__main__':
    with open('input.txt', 'r') as text:
        print(control_room(text, _SCREEN))
