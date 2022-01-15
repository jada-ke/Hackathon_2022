from flask import Flask, render_template
from inflation import *

app = Flask(__name__)

@app.route("/")
def home():
    infl, years, total_inflation = import_inflation_data("Data/inflation.csv", 2000)
    return render_template("index.html", years=years, inflation_values=infl, inflation_total=total_inflation)
    
if __name__ == "__main__":
    app.run(debug=True)