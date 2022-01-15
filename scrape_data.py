from numpy import string_
import pandas as pd
workbook= pd.read_csv(r"Data/2a71-das-wage2021opendata-esdc-all-19nov2021-vf.csv")
job= input(str("Please enter your job:"))
location= input(str("Please enter your location:"))
index= workbook.loc[(workbook["NOC_Title"]== job) & (workbook["PROV"]==location)]

print(index)
low_wage= index["Low_Wage_Salaire_Minium"].mean()
high_wage=index["High_Wage_Salaire_Maximal"].mean()
median_wage= index["Median_Wage_Salaire_Median"].mean()
print(low_wage, high_wage, median_wage)
