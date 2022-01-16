from flask import Flask, render_template, request
import requests
import pandas as pd
from inflation import import_inflation_data
from googlemaps import query_gmaps
from salary_distribution import salary_distribution
from find_titles_locations import find_jobtitles_locations

wage_file=r"Data/2a71-das-wage2021opendata-esdc-all-19nov2021-vf.csv"

app = Flask(__name__)

@app.route("/")
def home():
    jobs_list, locations_list = find_jobtitles_locations(wage_file)
    jobs_list = sorted(jobs_list)
    locations_list = sorted(locations_list[1:])
    for x, elem in enumerate(jobs_list): 
        if "'" in elem: jobs_list[x] = elem.replace("'", " ")
    return render_template("landingPage.html", jobs_list=str(jobs_list).replace("'", '"'), locations_list=str(locations_list[1:]).replace("'", '"'))

@app.route("/result", methods=['POST'])
def results():
    job = request.form.get('job')
    location = request.form.get('location')
    salary = float(request.form['salary'])
    time = int(request.form['time'])
    print(job, location, salary, time)

    with open('api_key.txt') as f:
        api_key = f.readline()
        f.close

    cumulative_infl, years, total_inflation, yearly_infl = import_inflation_data("Data/inflation.csv", time)

    print(job, location, salary, time)

    salary_distrib = salary_distribution(location, job, wage_file)
    print(salary_distrib)
    
    low_wage, median_wage, high_wage = (0, 0, 0)
    return render_template("result.html", low_wage=low_wage, median_wage=median_wage, high_wage=high_wage, years=years, cumulative_infl=cumulative_infl, yearly_infl=yearly_infl, inflation_total=total_inflation)

if __name__ == "__main__":
    app.run(debug=True)