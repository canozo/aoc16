import re


def triangle(t):
    count = 0
    for line in t:
        tri = [int(f) for f in re.findall(r"[\w']+", line)]
        condition = (
            tri[0] + tri[1] > tri[2],
            tri[0] + tri[2] > tri[1],
            tri[1] + tri[2] > tri[0]
        )
        if False not in condition:
            count += 1
    return count

if __name__ == '__main__':
    with open('input.txt', 'r') as _input:
        print(triangle(_input))
