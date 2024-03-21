import numpy as np

# a_x = -(D/m)vv_x
# a_y = -g - (D/m)vv_y
# D = pCA / 2 where p is the density of air, A is silhouette area A of bhe body (area seen at front while in motion),
# C is a constant called drag coefficient that depends on the shape of the body
#https://web.physics.wustl.edu/~wimd/topic01.pdf

def calculate_d(density_air, silhouette_area, drag_coefficient):
    return (density_air * silhouette_area * drag_coefficient) / 2


def calculate_ax(d, m, v, v_x):
    constant = (-d/m) * v_x
    return np.array(v) * constant


def calculate_ay(d, m, v, v_y):
    constant = 9.81 - ((d/m) * v_y)
    return np.array(v) * constant


# def calculate_new_x()
