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


def calculate_distance_at_peak(time_to_peak, v_ox):
    return time_to_peak * v_ox


def convert_to_metric_seconds(number, current_units):
    if current_units == 'ft':
        number *= 0.3048
    elif current_units == 'mi':
        number *= 1609.344
    elif current_units == 'km':
        number *= 1000
    elif current_units == 'ft/s':
        number *= 0.3048
    elif current_units == 'km/hr':
        number *= 1000
        number /= 3600
    elif current_units == 'mi/hr':
        number *= 1609.344
        number /= 3600
    elif current_units == 'deg':
        number = math.radians(number)
    elif current_units != 'm/s' and current_units != 'm' and current_units != 'rad':
        raise Exception("Invalid current_units input")
    return number


def convert_from_metric_seconds(number, target_units):
    if target_units == 'ft':
        number /= 0.3048
    elif target_units == 'mi':
        number /= 1609.344
    elif target_units == 'km':
        number /= 1000
    elif target_units == 'ft/s':
        number /= 0.3048
    elif target_units == 'km/hr':
        number /= 1000
        number *= 3600
    elif target_units == 'mi/hr':
        number /= 1609.344
        number *= 3600
    elif target_units == 'deg':
        number = math.degrees(number)
    elif target_units != 'm' and target_units != 'm/s' and target_units != 'rad':
        raise Exception("Invalid current_units input")
    return number


def convert_time(time, velocity_units):
    if velocity_units == 'm/s' or velocity_units == 'ft/s':
        return time, 's'
    elif velocity_units == 'mi/hr' or velocity_units == 'km/hr':
        return time / 3600, 'hr'
    else:
        raise Exception("invalid velocity entry that doesn't match options")