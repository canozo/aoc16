import re

database, history = {}, []


def process(text_file):
    v, i = [], []
    for line in text_file:
        if 'value' in line:
            v.append(line)
        else:
            i.append(line)
    return v, i


def puzzle(x, y):
    for line in values:
        value, bot = line.lstrip('value ').split(' goes to ')
        add_value(value, bot)
    return find_bot(x, y)


def add_value(value, bot):
    value = str(value)
    if bot in database and 'output' not in bot:
        database[bot].append(value)
        transfer_chips(bot)
    elif bot in database and 'output' in bot:
        database[bot].append(value)
    else:
        database[bot] = [value]


def transfer_chips(bot):
    line = [line for line in instructions if bot + ' gives' in line][0]
    _, takes_low, takes_high = re.split(' gives low to | and high to ', line)
    low, high = get_values(bot)
    add_value(low, takes_low)
    add_value(high, takes_high)
    database[bot].remove(str(low))
    database[bot].remove(str(high))


def get_values(bot):
    x, y = map(int, database[bot])
    history.append((bot, (x, y)))
    if x > y:
        return y, x
    else:
        return x, y


def find_bot(x, y):
    for element in history:
        bot, chips = element
        if x in chips and y in chips:
            return bot


if __name__ == '__main__':
    with open('input.txt') as text:
        values, instructions = process(text.read().split('\n'))
        print(puzzle(61, 17))
