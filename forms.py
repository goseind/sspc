from flask_wtf import FlaskForm
from wtfforms import DecimalField, StringField, SubmitField

class SavingsPlanCalculator(FlaskForm):
    new_capital = DecimalField('Available Capital')
    current_allocation_a = DecimalField('Asset Class A')
    current_allocation_b = DecimalField('Asset Class B')
    current_allocation_c = DecimalField('Asset Class C')
    current_allocation_d = DecimalField('Asset Class D')
    current_allocation_e = DecimalField('Asset Class E')
    calculate = SubmitField('Calculte new rates')