from flask import Flask, render_template, request
from inflation import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("landingPage.html")

@app.route("/results", methods=['POST'])
def results():
    job = request.form['job']
    location = request.form['location']
    salary = float(request.form['salary'])
    time = int(request.form['time'])
    print(job, location, salary, time)
    cumulative_infl, years, total_inflation, yearly_infl = import_inflation_data("Data/inflation.csv", time)
    return render_template("index.html", years=years, cumulative_infl=cumulative_infl, yearly_infl=yearly_infl, inflation_total=total_inflation)

if __name__ == "__main__":
    app.run(debug=True)