from scrape_data import read_data
from find_titles_locations import find_jobtitles_locations
from numpy import string_
import pandas as pd

wage_file=r"Data/2a71-das-wage2021opendata-esdc-all-19nov2021-vf.csv"
locations= find_jobtitles_locations(wage_file)[1]
job= input(str("Please enter your job:"))

def salary_distribution(locations, job):
    salary_dist={}
    for location in locations:
        min_salary=read_data(wage_file, job, location)[0]
        max_salary=read_data(wage_file, job, location)[1]
        salary_range= [min_salary, max_salary]
        salary_dist[location]=salary_range

    return salary_dist
