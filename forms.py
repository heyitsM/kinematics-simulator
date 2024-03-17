from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, SelectField
from wtforms.validators import data_required, number_range


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
