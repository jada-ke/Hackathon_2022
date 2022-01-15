from numpy import string_
import pandas as pd
workbook= pd.read_excel("2a71-das-wage2021opendata-esdc-all-19nov2021-vf")
job= input(str("Please entre your job"))
index= workbook["NOC_Title"]== job
workbook[index]