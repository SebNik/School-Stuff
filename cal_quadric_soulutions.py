# this program is calculating how many solutions a quadratic equation has
# https://edabit.com/challenge/o2AKq4xy3nfZabKXL
def solutions(a, b, c):
    # x coordinates of turning point
    x_1 = (-b * a) / 2
    x_2 = x_1 + 2
    y_1 = (a * x_1 ** 2) + b * x_1 + c
    y_2 = (a * x_2 ** 2) + b * x_2 + c
    if y_1 == 0:
        return 1
    if 0 < y_1 < y_2 or 0 > y_1 > y_2:
        return 0
    if 0 < y_1 and y_2 < y_1 or 0 > y_1 and y_2 > y_1:
        return 2
