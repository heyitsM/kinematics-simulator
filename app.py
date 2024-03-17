import math

from flask import Flask, render_template
from forms import VelocityAngleHeight
import kinemath
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/calculate', methods=['GET', 'POST'])
def do_math():
    form = VelocityAngleHeight()
    if form.validate_on_submit():
        initial_velocity = form.initial_velocity.data
        initial_height = form.initial_height.data
        final_height = form.final_surface_height.data
        launch_angle = form.launch_angle.data

        if form.rad_or_deg == 'deg':
            launch_angle = math.radians(launch_angle)

        v_ox, v_oy = kinemath.calculate_initial_velocities(initial_velocity, launch_angle)
        time_to_peak = kinemath.calculate_time_to_top(v_oy)
        height_at_peak = kinemath.calculate_height_at_peak(initial_height, v_oy, time_to_peak)

        if final_height <= height_at_peak:
            time_from_peak_to_ground = kinemath.calculate_time_from_peak_to_final(height_at_peak, final_height)
            valid_final_height = True
        else:
            time_from_peak_to_ground = kinemath.calculate_time_from_peak_to_final(height_at_peak, 0)
            valid_final_height = False

        total_time = time_to_peak + time_from_peak_to_ground
        x_distance_traveled = kinemath.get_total_x_distance(total_time, v_ox)

        return render_template('main.html', form=form, v_o=initial_velocity, y_o=initial_height,
                               final_height=final_height, valid_final_height=valid_final_height,
                               launch_angle=launch_angle, v_ox=v_ox, v_oy=v_oy,
                               peak_time=time_to_peak, peak_height=height_at_peak,
                               total_time=total_time, final_dist=x_distance_traveled )

    return render_template('main.html', form=form)

if __name__ == '__main__':
    app.run()
