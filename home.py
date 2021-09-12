from flask import Flask, render_template
from forms import SavingsPlanCalculator

app = Flask(__name__)
app.config['SECRET_KEY'] = '848f62f0482e1ea4ff7b03f8ba2205cf'

# Routing for root directory
@app.route("/")
def home():
    form = SavingsPlanCalculator()
    return render_template('savingsplan_calc.html', title='Calculator', form=form)

# Makes it possible to call the file directly with pyhton instead of using the debug mode
if __name__ == '__main__':
    app.run(debug=True)