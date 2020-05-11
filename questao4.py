import random
import time


def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)  # Calc the absolute y distance
    dx = abs(x1 - x0)  # CXalc the absolute x distance
    return dx == dy


def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(c):  # Look at all columns to the left of c
        if share_diagonal(i, bs[i], c, bs[c]):
            return True

    return False


def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1, len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False


def solve_four_twelve_sixteen():
    """Solves sizes 4 12 and 16 Queens Puzzle"""
    rng = random.Random()  # Instantiate a generator
    bd4 = list(range(4))
    bd12 = list(range(12))
    bd16 = list(range(16))  # Generate the initial permutation
    num_found = 0
    while num_found < 1:
        rng.shuffle(bd4)
        if not has_clashes(bd4):
            num_found += 1
    num_found = 0
    while num_found < 1:
        rng.shuffle(bd12)
        if not has_clashes(bd12):
            num_found += 1
    num_found = 0
    while num_found < 1:
        rng.shuffle(bd16)
        if not has_clashes(bd16):
            num_found += 1
    solutions = [bd4, bd12, bd16]
    return solutions


def solve_for_size(size):
    rng = random.Random()
    bd = list(range(size))  # Generate the initial permutation
    num_found = 0
    while num_found < 1:
        rng.shuffle(bd)
        if not has_clashes(bd):
            num_found += 1


def max_size():
    time_to_solve = 0
    size = 4
    while time_to_solve < 60:
        t1 = time.clock()
        solve_for_size(size)
        t2 = time.clock()
        time_to_solve = t2 - t1
        print(time_to_solve)
        size = size + 1
    return max_size()

print(max_size())