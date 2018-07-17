WALL = '#'
EMPTY = ' '
PATH = '*'
FIND = '$'
SIZE = 41


def generate_maze(puzzle_input, max_x=SIZE, max_y=SIZE):
    return [[is_wall(puzzle_input, x, y) for x in range(max_x)]
            for y in range(max_y)]


def is_wall(puzzle_input, x, y):
    the_sum = x*x + 3*x + 2*x*y + y + y*y + puzzle_input
    binary = to_binary(the_sum)
    if binary.count('1') % 2 == 0:
        return EMPTY
    else:
        return WALL


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
    return 0 <= x < SIZE and 0 <= y < SIZE \
           and maze[y][x] != WALL and maze[y][x] != PATH


def solve(maze, x=1, y=1):
    if can_move(maze, x, y):
        # we found the solution
        if maze[y][x] == FIND:
            print(f'There where {count_steps(maze)} steps done')
            return True

        # mark as temporary solution
        maze[y][x] = PATH

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
        maze[y][x] = EMPTY
        return False


def count_steps(maze):
    result = 0
    for line in maze:
        for square in line:
            if square == PATH:
                result += 1
    return result


def main():
    maze = generate_maze(1350)
    maze[39][31] = FIND
    solve(maze)


if __name__ == '__main__':
    main()
