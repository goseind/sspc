from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, SubmitField
from wtforms.validators import DataRequired

class SavingsPlanCalculator(FlaskForm):
    # General Fields (required)
    new_capital = DecimalField('Available Capital', validators=[DataRequired()])
    time_period = DecimalField('Time Period in Months', validators=[DataRequired()])

    # Asset Fields (min. two required)
    current_allocation_a = DecimalField('Asset Class A', validators=[DataRequired()])
    current_allocation_b = DecimalField('Asset Class B', validators=[DataRequired()])
    current_allocation_c = DecimalField('Asset Class C')
    current_allocation_d = DecimalField('Asset Class D')
    current_allocation_e = DecimalField('Asset Class E')

    # Functional Fields
    calculate = SubmitField('Calculte new rates')