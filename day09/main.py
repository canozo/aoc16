import re


def puzzle(file: str):
    init = ''
    parts = list(filter(None, re.split('(\\(|\\))', file)))
    for k, part in enumerate(parts):
        if 'x' in part:
            a, b = (int(j) for j in part.split('x'))
            rest = ''.join(map(str, [j for i, j in enumerate(parts) if i > k])).lstrip(')')
            latter = rest[:a] * b
            return init.rstrip('(') + latter + puzzle(rest[a:])
        else:
            init += part
    return init


def shameless_steal(line):
    amt = 0
    while line:
        next_id = re.match(r'(.*?)\((\d+)x(\d+)\)', line)
        if not next_id:
            break
        start, to_take, repeat = next_id.groups()
        to_take, repeat = int(to_take), int(repeat)
        amt += len(start)
        amt += shameless_steal(line[next_id.end():next_id.end() + to_take]) * repeat
        line = line[next_id.end() + to_take:]
    amt += len(line)
    return amt

if __name__ == '__main__':
    with open('input.txt', 'r') as text:
        # print(len(puzzle(text.read())))
        print(shameless_steal(text.read()))
