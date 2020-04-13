# this program is calculating how many solutions a quadratic equation has
# https://edabit.com/challenge/o2AKq4xy3nfZabKXL


def solutions(a, b, c):
    a = (b ** 2) - 4 * a * c
    if a > 0:
        return 2
    if a == 0:
        return 1
    if a < 0:
        return 0
