# Uses a lookup table rather than the * symbol to multiply

import math

def product(x: int, y: int) -> int:
    return sum([y for i in range(x)])

TABLE = {}

for i in range(10):
    for j in range(10):
        TABLE[(i, j)] = product(i, j)

def pad(number, side, length):
    if side == 'left':
        return length * '0' + number
    elif side == 'right':
        return number + length * '0'

def multiply(x: int, y: int) -> int:
    assert isinstance(x, int), 'x should be an integer.'
    assert isinstance(y, int), 'y should be an integer.'

    x = str(x)
    y = str(y)

    if len(x) == 1 and len(y) == 1:
        return TABLE[int(x), int(y)]

    if len(x) < len(y):
        x = pad(x, 'left', len(y)- len(x))
    elif len(y) < len(x):
        y = pad(y, 'left', len(x) - len(y))

    mid = math.floor(len(x) / 2)

    a = int(x[:mid])
    b = int(x[mid:])
    c = int(y[:mid])
    d = int(y[mid:])

    step1 = multiply(a, c)
    step2 = multiply(b, d)
    step3 = multiply(a + b, c + d)
    step4 = step3 - step2 - step1

    step1 = int(pad(str(step1), 'right', len(x) - mid + len(x) - mid))
    step4 = int(pad(str(step4), 'right', len(x) - mid))

    return step1 + step2 + step4