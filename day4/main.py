def obscure(file):
    total = 0
    for line in file:
        real = True
        save = False
        t = [x for x in line.rstrip('\n]').split('-')]
        checksum = t[-1].split('[')
        encrypted_name = ''.join(t[0:-1])

        for letter in checksum[1]:
            current = encrypted_name.count(letter)
            if save and ((save[1] < current) or (save[1] == current and letter < save[0]) or (current == 0)):
                real = False
                break
            save = (letter, current)

        if real:
            print(decrypt(' '.join(t[0:-1]), int(checksum[0])))
            total += int(checksum[0])
    return total


def decrypt(text, sector_id):
    decrypted_name = ''
    for char in text:
        if char == ' ':
            decrypted_name += char
            continue
        init_pos = sector_id + ord(char) - 97
        slid_pos = init_pos % 26
        decrypted_name += chr(slid_pos + 97)
    return decrypted_name, sector_id

if __name__ == '__main__':
    with open('input.txt', 'r') as _input:
        obscure(_input)
