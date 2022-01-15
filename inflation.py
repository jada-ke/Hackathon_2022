import pandas as pd

def import_inflation_data(filename, start_year):
    inflation_rates = pd.read_csv(filename, sep = "\t")
    row_nbr = 2021-start_year
    
    infl = [inflation_rates.iloc[row_nbr]["inflation"]]
    for x in range(row_nbr-1, -1, -1):
        infl.append(((1+infl[-1]/100)*(1+inflation_rates.iloc[x]["inflation"]/100)-1)*100)
    for x, elem in enumerate(infl):
        infl[x] = round(elem, 2)
    years = [2021-x for x in range(row_nbr, -1, -1)]
    total_inflation = infl[-1]

    return infl, years, total_inflation