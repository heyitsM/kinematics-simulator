import numpy as np

def slope(point_1, point_2):
    if point_2[0] - point_1[0] == 0:
        raise Exception('Two x-coordinates may not be the same- this implies undefined slope')

    return (point_2[1] - point_1[1]) / (point_2[0] - point_1[0])

def y_intercept(slp, point):
    x = point[0]
    y = point[1]
    y_int = y - (slp * x)

    return 0, y_int

def x_intercept(m, b):
    return -b[1] / m, 0


def calc_y(m, b, x):
    return m*x + b[1]


def generate_data(m, b, xint):
    if xint[0] < 0:
        base_x = np.array(range(int(xint[0]) - 10, 11))
    elif xint[0] > 0:
        base_x = np.array(range(-10, int(xint[0]) + 11))
    else:
        base_x = np.array(range(-10, 11))

    y = calc_y(m, b, base_x)
    y = zip(base_x, list(y))
    y = map(lambda x: {'x': float(x[0]), 'y': float(x[1])}, tuple(y))
    return list(y)

