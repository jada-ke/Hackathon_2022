from flask import Flask, render_template
from inflation import *

app = Flask(__name__)

@app.route("/")
def home():
    cumulative_infl, years, total_inflation, yearly_infl = import_inflation_data("Data/inflation.csv", 2000)
    return render_template("index.html", years=years, cumulative_infl=cumulative_infl, yearly_infl=yearly_infl, inflation_total=total_inflation)
    
if __name__ == "__main__":
    app.run(debug=True)