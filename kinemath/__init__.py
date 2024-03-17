import math


def calculate_initial_velocities(v_o, theta):
    v_oy = v_o * math.sin(theta)
    v_ox = v_o * math.cos(theta)

    return [v_ox, v_oy]


def calculate_time_to_top(v_oy):
    return v_oy / 9.81


def calculate_height_at_peak(y_o, v_oy, t):
    return y_o + (v_oy * t) + (0.5 * -9.81 * t**2)


def calculate_time_from_peak_to_final(y_o, y_f):
    return math.sqrt(2 * ((y_f - y_o) / -9.81))


def get_total_x_distance(t, v_ox):
    return t * v_ox

