from numpy import string_
import pandas as pd
wage_file=r"Data/2a71-das-wage2021opendata-esdc-all-19nov2021-vf.csv"

def find_jobtitles_locations(wage_file):
    workbook= pd.read_csv(wage_file)
    jobs= workbook["NOC_Title"].tolist()
    locations=workbook["PROV"].tolist()
    jobs=list(dict.fromkeys(jobs))
    locations= list(dict.fromkeys(locations))

    return jobs, locations
