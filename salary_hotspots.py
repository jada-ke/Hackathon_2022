from cmath import nan
import pandas as pd
from find_titles_locations import find_jobtitles_locations
from googlemaps import query_gmaps
from gmap_to_img import gmapscoord_to_imgpixel
from scrape_data import get_job_placesss
from PIL import Image, ImageDraw

wage_file=r"Data/2a71-das-wage2021opendata-esdc-all-19nov2021-vf.csv"
#im.show()
locations= find_jobtitles_locations(wage_file)[1]
standard_size= 100

def isNaN(array):
    for x in array: 
        if x != x: return True
    return False

def get_data_by_place(wage_file, job):
    locations = get_job_placesss(wage_file, job)
    loc_wage_dict = {}
    workbook= pd.read_csv(wage_file)
    for x in locations:
        index= workbook.loc[(workbook["NOC_Title"] == job) & (workbook["ER_Name_Nom_RE"] == x)]
        tmp = [index["Low_Wage_Salaire_Minium"].mean(), index["High_Wage_Salaire_Maximal"].mean(), index["Median_Wage_Salaire_Median"].mean()]
        if not isNaN(tmp):
            loc_wage_dict[x] = tmp
    return loc_wage_dict

def get_median(salary_dist):
    keys=list(salary_dist.keys())
    values=list(salary_dist.values())
    median_salaries={}
    for i in range(len(values)):
        median=values[i][1]
        median_salaries[keys[i]]=median
    return median_salaries

def scale_circle(standard_size, job, wage_file):
    median_salaries=get_median(get_data_by_place(wage_file, job))
    circle_dimensions={}
    ave_median= sum(median_salaries.values())/len(median_salaries)
    for location in median_salaries:
        circle_size= (median_salaries[location]/ave_median)*standard_size
        circle_dimensions[location]=circle_size
    return circle_dimensions

def place_hotspot(draw, api_key, job, wage_file):
    circle_dim= scale_circle(standard_size, job, wage_file)
    for location in circle_dim.keys():
        coord = query_gmaps(location, api_key)
        lat_coord= coord["lat"]
        long_coord= coord["lng"]

        pixel_coord=list(gmapscoord_to_imgpixel(lat_coord, long_coord).values()) 
        print(pixel_coord)

        loc_size=circle_dim[location]

        xy = (pixel_coord[0]-1/2*loc_size, pixel_coord[1]-1/2*loc_size, pixel_coord[0]+1/2*loc_size, pixel_coord[1]+1/2*loc_size)
        draw.ellipse(xy, fill=(255, 90, 90), outline=(255, 50, 50))
    
#with open('api_key.txt') as f:
#        api_key = f.readline()
#        f.close
#place_hotspot(["Ontario"], draw, api_key, "Legislators", wage_file)
#im.show()