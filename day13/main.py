solutions = []
wall = '#'
empty = '.'
path = 'O'
find = '$'
max_size = 41


def generate_maze(puzzle_input, max_x=max_size, max_y=max_size):
    return [[is_wall(puzzle_input, x, y) for x in range(max_x)]
            for y in range(max_y)]


def is_wall(puzzle_input, x, y):
    the_sum = x*x + 3*x + 2*x*y + y + y*y + puzzle_input
    binary = to_binary(the_sum)
    if binary.count('1') % 2 == 0:
        return empty
    else:
        return wall


def to_binary(num):
    binary = ""
    while num > 0:
        if num % 2 == 0:
            binary = '0' + binary
        else:
            binary = '1' + binary
        num //= 2
    return binary


def can_move(maze, x, y):
    return 0 <= x < max_size and 0 <= y < max_size \
           and maze[y][x] != wall and maze[y][x] != path


def solve(maze, x=1, y=1):
    if can_move(maze, x, y):
        # we found the solution
        if maze[y][x] == find:
            solutions.append(count_steps(maze))
            # always return false when finding a solution
            # since we're looking for the shortest path
            return False

        # mark as temporary solution
        maze[y][x] = path

        # move up
        if solve(maze, x, y + 1):
            return True

        # move down
        if solve(maze, x, y - 1):
            return True

        # move left
        if solve(maze, x - 1, y):
            return True

        # move right
        if solve(maze, x + 1, y):
            return True

        # dead end, unmark as solution
        maze[y][x] = empty
        return False


def solve_enterprise_edition(maze, x=1, y=1, steps=0):
    if can_move(maze, x, y):
        if steps <= 50:
            coord = (x, y)
            if coord not in solutions:
                solutions.append(coord)
        else:
            return False

        # mark as temporary solution
        maze[y][x] = path
        steps += 1

        # move up
        if solve_enterprise_edition(maze, x, y + 1, steps):
            return True

        # move down
        if solve_enterprise_edition(maze, x, y - 1, steps):
            return True

        # move left
        if solve_enterprise_edition(maze, x - 1, y, steps):
            return True

        # move right
        if solve_enterprise_edition(maze, x + 1, y, steps):
            return True

        # dead end, unmark as solution
        maze[y][x] = empty
        steps -= 1
        return False


def count_steps(maze):
    result = 0
    for line in maze:
        for square in line:
            if square == path:
                result += 1
    return result


def print_maze(maze):
    print(count_steps(maze))
    for line in maze:
        for char in line:
            print(char, end='')
        print()
    print('\n\n')


def main():
    maze = generate_maze(1350)
    maze[39][31] = find

    part = int(input('part: '))

    if part == 1:
        solve(maze)
        print(f'Shortest path to solution: {min(solutions)}')
    elif part == 2:
        solve_enterprise_edition(maze)
        print(f'Locations reached with 50 steps: {len(solutions)}')


if __name__ == '__main__':
    main()
