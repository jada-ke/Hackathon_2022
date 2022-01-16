import pandas as pd

def read_data(wage_file, job, location):
    workbook= pd.read_csv(wage_file)
    index= workbook.loc[(workbook["NOC_Title"]== job) & (workbook["PROV"]==location)]

    low_wage= index["Low_Wage_Salaire_Minium"].mean()
    high_wage=index["High_Wage_Salaire_Maximal"].mean()
    median_wage= index["Median_Wage_Salaire_Median"].mean()
    
    return low_wage, high_wage, median_wage

def get_job_overall_mean(wage_file, job):
    workbook= pd.read_csv(wage_file)
    index= workbook.loc[(workbook["NOC_Title"]== job)]

    low_wage= index["Low_Wage_Salaire_Minium"].mean()
    high_wage=index["High_Wage_Salaire_Maximal"].mean()
    median_wage= index["Median_Wage_Salaire_Median"].mean()
    
    return {"low_wage" :low_wage, "high_wage" : high_wage, "median_wage" : median_wage }

def get_job_provinces(wage_file, job):
    workbook= pd.read_csv(wage_file)
    index= workbook.loc[(workbook["NOC_Title"]== job)]

    locations = index["PROV"]
    
    return locations

def get_job_placesss(wage_file, job):
    workbook= pd.read_csv(wage_file)
    index= workbook.loc[(workbook["NOC_Title"]== job)]

    locations = index["ER_Name_Nom_RE"]
    
    return locations