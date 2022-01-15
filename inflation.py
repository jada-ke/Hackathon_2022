import matplotlib.pyplot as plt
import pandas as pd

def import_inflation_data(filename, start_year):
    inflation_rates = pd.read_csv(filename, sep = "\t")
    row_nbr = 2021-start_year
    
    infl = [100]
    for x in range(row_nbr-1, -1, -1):
        infl.append(infl[-1]*(1+inflation_rates.iloc[x]["inflation"]/100))
    years = [2021-x for x in range(row_nbr, -1, -1)]
    total_inflation = infl[-1]/100

    return infl, years, total_inflation