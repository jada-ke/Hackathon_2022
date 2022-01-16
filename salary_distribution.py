from scrape_data import read_data
from find_titles_locations import find_jobtitles_locations
from numpy import string_
import pandas as pd

def salary_distribution(locations, job, wage_file):
    salary_dist={}
    for location in locations:
        min_salary=read_data(wage_file, job, location)[0]
        median_salary=read_data(wage_file, job, location)[2]
        max_salary=read_data(wage_file, job, location)[1]
        salary_range= [min_salary, max_salary, median_salary]
        salary_dist[location]=salary_range

    return salary_dist
