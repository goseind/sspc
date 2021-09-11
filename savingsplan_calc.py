from flask import Flask

app = Flask(__name__)

@app.route("/")
def savingsplan_calc():
    return "<h1>Simple Savings Plan Calculator</h1>"
