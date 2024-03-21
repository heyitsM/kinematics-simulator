from flask import Flask, render_template
from forms import VelocityAngleHeight, TwoPointsLine, PointSlope
import kinemath
import os
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/basic-kinematics', methods=['GET', 'POST'])
def do_kinematics():
    form = VelocityAngleHeight(metric_or_imperial='m', velocity_units='m/s', rad_or_deg='deg',
                               final_metric_or_imperial='m', final_velocity_units='m/s', final_rad_or_deg='deg')
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

        launch_angle = kinemath.basic.convert_to_metric_seconds(launch_angle, rad_or_deg)
        initial_velocity = kinemath.basic.convert_to_metric_seconds(initial_velocity, velocity_units)
        initial_height = kinemath.basic.convert_to_metric_seconds(initial_height, metric_or_imperial)
        final_height = kinemath.basic.convert_to_metric_seconds(final_height, metric_or_imperial)

        v_ox, v_oy = kinemath.basic.calculate_initial_velocities(initial_velocity, launch_angle)
        time_to_peak = kinemath.basic.calculate_time_to_top(v_oy)
        height_at_peak = kinemath.basic.calculate_height_at_peak(initial_height, v_oy, time_to_peak)
        x_distance_at_peak = kinemath.basic.calculate_distance_at_peak(time_to_peak, v_ox)

        if final_height <= height_at_peak:
            time_from_peak_to_ground = kinemath.basic.calculate_time_from_peak_to_final(height_at_peak, final_height)
            valid_final_height = True
        else:
            time_from_peak_to_ground = kinemath.basic.calculate_time_from_peak_to_final(height_at_peak, 0)
            valid_final_height = False

        total_time = time_to_peak + time_from_peak_to_ground
        x_distance_traveled = kinemath.basic.get_total_x_distance(total_time, v_ox)

        initial_velocity = kinemath.basic.convert_from_metric_seconds(initial_velocity, final_velocity_units)
        initial_height = kinemath.basic.convert_from_metric_seconds(initial_height, final_metric_or_imperial)
        final_height = kinemath.basic.convert_from_metric_seconds(final_height, final_metric_or_imperial)
        launch_angle = kinemath.basic.convert_from_metric_seconds(launch_angle, final_rad_or_deg)

        v_ox = kinemath.basic.convert_from_metric_seconds(v_ox, final_velocity_units)
        v_oy = kinemath.basic.convert_from_metric_seconds(v_oy, final_velocity_units)
        height_at_peak = kinemath.basic.convert_from_metric_seconds(height_at_peak, final_metric_or_imperial)
        x_distance_at_peak = kinemath.basic.convert_from_metric_seconds(x_distance_at_peak, final_metric_or_imperial)
        x_distance_traveled = kinemath.basic.convert_from_metric_seconds(x_distance_traveled, final_metric_or_imperial)

        time_to_peak = kinemath.basic.convert_time(time_to_peak, final_velocity_units)
        total_time = kinemath.basic.convert_time(total_time, final_velocity_units)

        coords = kinemath.graphing.generate_coordinates(initial_height, 0,
                                                      v_oy, v_ox, total_time[0], total_time[0] / 1000)
        print(type(coords))
        print(type(coords[0]))
        print(type(coords[0]['x']))
        return render_template('kinematics.html', form=form, v_o=initial_velocity, y_o=initial_height,
                               final_height=final_height, valid_final_height=valid_final_height,
                               launch_angle=launch_angle, v_ox=v_ox, v_oy=v_oy,
                               peak_time=time_to_peak[0], peak_height=height_at_peak, peak_distance=x_distance_at_peak,
                               total_time=total_time[0], final_dist=x_distance_traveled,
                               vel_units=velocity_units, dist_units=metric_or_imperial, deg_units=rad_or_deg,
                               final_vel_units=final_velocity_units, final_dist_units=final_metric_or_imperial,
                               final_deg_units=final_rad_or_deg, time_units=total_time[1],
                               coords=coords, scroll='solutions')

    return render_template('kinematics.html', form=form)

@app.route('/line-equation', methods=['GET', 'POST'])
def line_equation():
    formT = TwoPointsLine()
    formP = PointSlope()

    if formT.submitT.data and formT.validate_on_submit():
        point_1 = (formT.x_1.data, formT.y_1.data)
        point_2 = (formT.x_2.data, formT.y_2.data)
        slope = kinemath.linear.slope(point_1, point_2)
        y_intercept = kinemath.linear.y_intercept(slope, point_1)
        x_intercept = kinemath.linear.x_intercept(slope, y_intercept)
        coords = kinemath.linear.generate_data(slope, y_intercept, x_intercept)

        return render_template('line_equations.html', point_1=point_1,
                               point_2=point_2, slope=slope, form=formT, form2=formP, y_int=y_intercept,
                               x_int=x_intercept, coords=coords, scroll='solutions')

    if formP.submitP.data and formP.validate_on_submit():
        point_1 = (formP.x.data, formP.y.data)
        slope = formP.m.data
        y_intercept = kinemath.linear.y_intercept(slope, point_1)
        x_intercept = kinemath.linear.x_intercept(slope, y_intercept)
        coords = kinemath.linear.generate_data(slope, y_intercept, x_intercept)

        return render_template('line_equations.html', point=point_1, slope=slope, form=formT, form2=formP,
                               y_int=y_intercept, x_int=x_intercept, coords=coords, scroll='solutions')

    return render_template('line_equations.html', form=formT, form2=formP)


if __name__ == '__main__':
    app.run()
