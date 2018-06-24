def dragon_curve(data):
    data_b = list(data[::-1])
    for i, char in enumerate(data_b):
        if char == '1':
            data_b[i] = '0'
            continue
        data_b[i] = '1'
    return data + '0' + ''.join(data_b)


def generate_checksum(data):
    while len(data) % 2 == 0:
        pairs = [data[x:x+2] for x in range(0, len(data), 2)]
        save = []
        for p in pairs:
            if p[0] == p[1]:
                save.append('1')
                continue
            save.append('0')
        data = ''.join(save)
    return data


def puzzle(data, length):
    print('dragon curve... ')
    while len(data) < length:
        data = dragon_curve(data)
    data = data[:length]
    print('generating checksum... ')
    return generate_checksum(data)

if __name__ == '__main__':
    print(puzzle('01000100010010111', 35651584))
