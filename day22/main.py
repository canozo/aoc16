def process_list(puzzle):
    nodes = []
    for line in puzzle:
        cord, size, used, avail, perc = line.strip().split()

        xi = cord.index('x')
        yi = cord.index('y')

        x = int(cord[xi + 1:yi - 1])
        y = int(cord[yi + 1:])

        items = (size, used, avail, perc)
        size, used, avail, perc = (int(x[:-1]) for x in items)

        nodes.append((x, y, size, used, avail))
    return nodes


def count_viable_nodes(database):
    count = 0
    for i in range(len(database)):
        for j in range(len(database)):
            if i == j:
                continue

            a = database[i]
            b = database[j]
            if a[3] != 0 and a[3] <= b[-1]:
                count += 1
    return count


def process_grid(puzzle):
    # find max x and y
    cord = puzzle[-1].strip().split()[0]

    xi = cord.index('x')
    yi = cord.index('y')

    max_x = int(cord[xi + 1:yi - 1])
    max_y = int(cord[yi + 1:])

    grid = [[None for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for line in puzzle:
        cord, size, used, avail, perc = line.strip().split()

        xi = cord.index('x')
        yi = cord.index('y')

        x = int(cord[xi + 1:yi - 1])
        y = int(cord[yi + 1:])

        items = (size, used, avail, perc)
        size, used, avail, perc = (int(x[:-1]) for x in items)

        grid[y][x] = (size, used, avail)
    return grid


def solve(grid):
    max_y, max_x = len(grid), len(grid[0])


def main():
    part = int(input('part: '))

    with open('input.txt', 'r') as puzzle_file:
        puzzle = puzzle_file.read().splitlines()

    if part == 1:
        database = process_list(puzzle)
        print(count_viable_nodes(database))
    elif part == 2:
        grid = process_grid(puzzle)
        print(solve(grid))


if __name__ == '__main__':
    main()
