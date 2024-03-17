from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, SelectField
from wtforms.validators import data_required, number_range


class VelocityAngleHeight(FlaskForm):
    initial_velocity = FloatField('Initial Velocity', validators=[data_required(), number_range(0)])
    launch_angle = FloatField('Launch Angle', validators=[data_required(), number_range(0, 360)])
    rad_or_deg = SelectField('Angle Format', validators=[data_required()], choices=[('rad', 'Radians'), ('deg', 'Degrees')])
    initial_height = FloatField('Initial Height', validators=[data_required(), number_range(0)])
    final_surface_height = FloatField('Final Height', validators=[data_required(), number_range(0)])
    submit = SubmitField('Submit')
