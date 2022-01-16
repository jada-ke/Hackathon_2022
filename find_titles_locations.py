import pandas as pd


def find_jobtitles_locations(wage_file):
    workbook= pd.read_csv(wage_file)
    jobs= workbook["NOC_Title"].tolist()
    locations=workbook["PROV"].tolist()
    jobs=list(dict.fromkeys(jobs))
    locations= list(dict.fromkeys(locations))

    return jobs, locations
