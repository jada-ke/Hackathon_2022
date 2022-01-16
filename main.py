from flask import Flask, render_template, request
import requests
import pandas as pd
from inflation import import_inflation_data
from googlemaps import query_gmaps
from salary_distribution import salary_distribution
from find_titles_locations import find_jobtitles_locations
from scrape_data import get_job_overall_mean, read_data, get_job_places

wage_file=r"Data/2a71-das-wage2021opendata-esdc-all-19nov2021-vf.csv"

app = Flask(__name__)


jobs_list, locations_list = find_jobtitles_locations(wage_file)
jobs_list = sorted(jobs_list)
locations_list = sorted(locations_list[1:])
for x, elem in enumerate(jobs_list): 
    if "'" in elem: jobs_list[x] = elem.replace("'", " ")

@app.route("/")
def home():
    return render_template("landingPage.html", 
    jobs_list=str(jobs_list).replace("'", '"'), 
    locations_list=str(locations_list[1:]).replace("'", '"'))

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

    salary_distrib = get_job_overall_mean(wage_file, job)
    salary_distrib_prov = salary_distribution([location], job, wage_file)[location]
    
    if salary == salary_distrib["median_wage"]: salary_comp = "the same as"
    elif salary < salary_distrib["median_wage"]: salary_comp = "under"
    else: salary_comp = "above"

    if salary == salary_distrib_prov[2]: salary_comp_prov = "the same as"
    elif salary < salary_distrib_prov[2]: salary_comp_prov = "under"
    else: salary_comp_prov = "above"

    return render_template("result.html",
    job_name=job,
    salary_comp=salary_comp,
    low_wage=round(salary_distrib["low_wage"], 2),
    median_wage=round(salary_distrib["median_wage"], 2),
    high_wage=round(salary_distrib["high_wage"], 2),
    salary_comp_prov=salary_comp_prov,
    low_wage_prov=round(salary_distrib_prov[0], 2),
    median_wage_prov=round(salary_distrib_prov[2], 2),
    high_wage_prov=round(salary_distrib_prov[1], 2),
    years=years, 
    cumulative_infl=cumulative_infl, 
    yearly_infl=yearly_infl, 
    inflation_total=total_inflation)

if __name__ == "__main__":
    app.run(debug=True)