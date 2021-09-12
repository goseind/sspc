from flask import Flask, render_template

app = Flask(__name__)

# Routing for root directory
@app.route("/")
def home():
    form = SavingsPlanCalculator()
    return render_template('savingsplan_calc.html', title='Calculator', form=form)

# Makes it possible to call the file directly with pyhton instead of using the debug mode
if __name__ == '__main__':
    app.run(debug=True)