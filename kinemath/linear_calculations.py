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

# def generate_data(m, b, xint):
