import hashlib


def md5_encode(string):
    return hashlib.md5(string.encode('utf-8')).hexdigest()


def checkers(test, array):
    if test.isdigit():
        t = int(test)
        return 0 <= t <= 7 and array[t] is None
    else:
        return False


def puzzle(door_id):
    answer = ''
    index = 0
    while len(answer) < 8:
        t = md5_encode(door_id + str(index))
        if t[:5] == '00000':
            answer += t[5]
            print('{}, {}, {}'.format(t, index, answer))
        index += 1
    return answer


def puzzle_revindicated(door_id):
    answer = [None for _ in range(8)]
    index = 0
    while None in answer:
        t = md5_encode(door_id + str(index))
        if t[:5] == '00000' and checkers(t[5], answer):
            answer[int(t[5])] = t[6]
            print('{}, {}, {}'.format(t, index, answer))
        index += 1
    return ''.join(map(str, answer))

_INPUT = 'ojvtpuvg'

if __name__ == '__main__':
    print(puzzle_revindicated(_INPUT))
