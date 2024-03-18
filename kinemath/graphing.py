import numpy as np
import matplotlib as plt
from bokeh.embed import components
from bokeh.plotting import figure

g = -9.81


def calculate_y_position(y_o, v_oy, t):
    second_term = v_oy * t
    third_term = 0.5 * g * (t**2)
    return y_o + second_term + third_term


def calculate_x_position(x_o, v_ox, t):
    second_term = v_ox * t
    return x_o + second_term


def generate_coordinates(y_o, x_o, v_oy, v_ox, max_time, interval):
    start_time = 0
    x_pos = []
    y_pos = []
    coordinates = []

    while start_time < max_time:
        x = calculate_x_position(x_o, v_ox, start_time)
        y = calculate_y_position(y_o, v_oy, start_time)
        x_pos.append(x)
        y_pos.append(y)
        coordinates.append({'x': x, 'y': y})

        start_time += interval
    # return x_pos, y_pos
    return coordinates


