import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
from salary_distribution import salary_distribution
from find_titles_locations import find_jobtitles_locations
from googlemaps import query_gmaps
from gmap_to_img import gmapscoord_to_imgpixel

wage_file=r"Data/2a71-das-wage2021opendata-esdc-all-19nov2021-vf.csv"
img= plt.imread("static/image_3.png")
locations= find_jobtitles_locations(wage_file)[1]
job=input(str("Please enter your job:"))
salary_dist=salary_distribution(locations, job)
standard_size= 100
figure, axes= plt.subplots()
axes.set_aspect("equal")


def get_median(salary_dist):
    keys=list(salary_dist.keys())
    values=list(salary_dist.values())
    median_salaries={}
    for i in range(len(values)):
        median=values[i][1]
        median_salaries[keys[i]]=median
    return median_salaries

def scale_circle(standard_size):
    median_salaries=get_median(salary_dist)
    circle_dimensions={}
    ave_median= sum(median_salaries.values())/len(median_salaries)
    for location in median_salaries:
        circle_size= (median_salaries[location]/ave_median)*standard_size
        circle_dimensions[location]=circle_size
    return circle_dimensions

def place_hotspot(locations, img):
    circle_dim= scale_circle(standard_size)
    for location in locations:
        lat_coord= query_gmaps["lat"]
        long_coord= query_gmaps["lng"]
        pixel_coord=list(gmapscoord_to_imgpixel(lat_coord, long_coord).values()) 
        loc_size=circle_dim[location]
        circle= plt.Circle((pixel_coord[0], pixel_coord[1]), loc_size, alpha=0.6, color="black")
        axes.add_patch(circle)
    plt.show()
    

