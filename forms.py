from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, SelectField
from wtforms.validators import input_required, data_required, number_range


class VelocityAngleHeight(FlaskForm):
    metric_or_imperial = SelectField('Distance Format', choices=[('ft', 'Imperial (feet)'),
                                                                 ('mi', 'Imperial (miles)'),
                                                                 ('m', 'Metric (meters)'),
                                                                 ('km', 'Metric (kilometers)')],
                                     validators=[data_required()])
    velocity_units = SelectField('Velocity Format', choices=[('m/s', 'Meters per Second (m/s)'),
                                                             ('ft/s', 'Feet per Second (ft/s)'),
                                                             ('mi/hr', 'Miles per Hour (mph)'),
                                                             ('km/hr', 'Kilometers per Hour (kph)')],
                                 validators=[data_required()])
    rad_or_deg = SelectField('Angle Format',
                             validators=[data_required()], choices=[('rad', 'Radians'), ('deg', 'Degrees')])

    final_metric_or_imperial = SelectField('Result Distance Format', choices=[('ft', 'Imperial (feet)'),
                                                                       ('mi', 'Imperial (miles)'),
                                                                       ('m', 'Metric (meters)'),
                                                                       ('km', 'Metric (kilometers)')],
                                           validators=[data_required()])
    final_velocity_units = SelectField('Result Velocity Format', choices=[('m/s', 'Meters per Second (m/s)'),
                                                                   ('ft/s', 'Feet per Second (ft/s)'),
                                                                   ('mi/hr', 'Miles per Hour (mph)'),
                                                                   ('km/hr', 'Kilometers per Hour (kph)')],
                                       validators=[data_required()])
    final_rad_or_deg = SelectField('Result Angle Format',
                                   validators=[data_required()], choices=[('rad', 'Radians'), ('deg', 'Degrees')])
    initial_velocity = FloatField('Initial Velocity', validators=[number_range(0)])
    launch_angle = FloatField('Launch Angle', validators=[number_range(0, 360)])

    initial_height = FloatField('Initial Height', validators=[number_range(0)])
    final_surface_height = FloatField('Final Height', validators=[number_range(0)])
    submit = SubmitField('Submit')

class TwoPointsLine(FlaskForm):
    x_1 = FloatField('X1 coordinate', validators=[input_required()])
    y_1 = FloatField('Y1 coordinate', validators=[input_required()])
    x_2 = FloatField('X2 coordinate', validators=[input_required()])
    y_2 = FloatField('Y2 coordinate', validators=[input_required()])
    submitT = SubmitField('Submit')

class PointSlope(FlaskForm):
    x = FloatField('X coordinate', validators=[input_required()])
    y = FloatField('Y coordinate', validators=[input_required()])
    m = FloatField('Slope', validators=[input_required()])
    submitP = SubmitField('Submit')
