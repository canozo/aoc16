_input = '......^.^^.....^^^^^^^^^...^.^..^^.^^^..^.^..^.^^^.^^^^..^^.^.^.....^^^^^..^..^^^..^^.^.^..^^..^^^..'


def generate_traps(first_floor, rows):
    f_max = len(first_floor)
    floors = [first_floor]

    for x in range(1, rows):
        prev_f, curr_f = x - 1, x
        save = []

        for i, char in enumerate(floors[prev_f]):
            if i == 0:
                # left_exists, right_exists = False, True
                top_tiles = '.' + floors[prev_f][i:i+2]
            elif i+1 == f_max:
                # left_exists, right_exists = True, False
                top_tiles = floors[prev_f][i-1:i+1] + '.'
            else:
                # left_exists, right_exists = True, True
                top_tiles = floors[prev_f][i-1:i+2]

            if top_tiles in ('^^.', '.^^', '..^', '^..'):
                save.append('^')
                continue
            save.append('.')

        # print(''.join(save), x)
        floors.append(''.join(save))

    return ''.join(floors).count('.')

if __name__ == '__main__':
    print('working... ')
    print(generate_traps(_input, 400000))
