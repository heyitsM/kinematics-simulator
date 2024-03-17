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
        velocity_units = form.velocity_units.data
        metric_or_imperial = form.metric_or_imperial.data
        rad_or_deg = form.rad_or_deg.data
        final_velocity_units = form.final_velocity_units.data
        final_metric_or_imperial = form.final_metric_or_imperial.data
        final_rad_or_deg = form.final_rad_or_deg.data

        launch_angle = kinemath.convert_to_metric_seconds(launch_angle, rad_or_deg)
        initial_velocity = kinemath.convert_to_metric_seconds(initial_velocity, velocity_units)
        initial_height = kinemath.convert_to_metric_seconds(initial_height, metric_or_imperial)
        final_height = kinemath.convert_to_metric_seconds(final_height, metric_or_imperial)

        v_ox, v_oy = kinemath.calculate_initial_velocities(initial_velocity, launch_angle)
        time_to_peak = kinemath.calculate_time_to_top(v_oy)
        height_at_peak = kinemath.calculate_height_at_peak(initial_height, v_oy, time_to_peak)
        x_distance_at_peak = kinemath.calculate_distance_at_peak(time_to_peak, v_ox)

        if final_height <= height_at_peak:
            time_from_peak_to_ground = kinemath.calculate_time_from_peak_to_final(height_at_peak, final_height)
            valid_final_height = True
        else:
            time_from_peak_to_ground = kinemath.calculate_time_from_peak_to_final(height_at_peak, 0)
            valid_final_height = False

        total_time = time_to_peak + time_from_peak_to_ground
        x_distance_traveled = kinemath.get_total_x_distance(total_time, v_ox)

        initial_velocity = kinemath.convert_from_metric_seconds(initial_velocity, final_velocity_units)
        initial_height = kinemath.convert_from_metric_seconds(initial_height, final_metric_or_imperial)
        final_height = kinemath.convert_from_metric_seconds(final_height, final_metric_or_imperial)
        launch_angle = kinemath.convert_from_metric_seconds(launch_angle, final_rad_or_deg)

        v_ox = kinemath.convert_from_metric_seconds(v_ox, final_velocity_units)
        v_oy = kinemath.convert_from_metric_seconds(v_oy, final_velocity_units)
        height_at_peak = kinemath.convert_from_metric_seconds(height_at_peak, final_metric_or_imperial)
        x_distance_at_peak = kinemath.convert_from_metric_seconds(x_distance_at_peak, final_metric_or_imperial)
        x_distance_traveled = kinemath.convert_from_metric_seconds(x_distance_traveled, final_metric_or_imperial)

        time_to_peak = kinemath.convert_time(time_to_peak, final_velocity_units)
        total_time = kinemath.convert_time(total_time, final_velocity_units)

        return render_template('main.html', form=form, v_o=initial_velocity, y_o=initial_height,
                               final_height=final_height, valid_final_height=valid_final_height,
                               launch_angle=launch_angle, v_ox=v_ox, v_oy=v_oy,
                               peak_time=time_to_peak[0], peak_height=height_at_peak, peak_distance=x_distance_at_peak,
                               total_time=total_time[0], final_dist=x_distance_traveled,
                               vel_units=velocity_units, dist_units=metric_or_imperial, deg_units=rad_or_deg,
                               final_vel_units=final_velocity_units, final_dist_units=final_metric_or_imperial,
                               final_deg_units=final_rad_or_deg, time_units=total_time[1])

    return render_template('main.html', form=form)

if __name__ == '__main__':
    app.run()
