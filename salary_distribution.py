from scrape_data import read_data
from find_titles_locations import find_jobtitles_locations
import pandas as pd

def salary_distribution(locations, job, wage_file):
    salary_dist={}
    for location in locations:
        salary_range = read_data(wage_file, job, location)
        salary_dist[location] = salary_range

    return salary_dist
