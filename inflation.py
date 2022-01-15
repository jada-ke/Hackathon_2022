import pandas as pd

def import_inflation_data(filename, start_year):
    inflation_rates = pd.read_csv(filename, sep = "\t")
    row_nbr = 2021-start_year
    
    cumulative_infl = [inflation_rates.iloc[row_nbr]["inflation"]]
    yearly_infl = [inflation_rates.iloc[row_nbr]["inflation"]]
    for x in range(row_nbr-1, -1, -1):
        cumulative_infl.append(((1+cumulative_infl[-1]/100)*(1+inflation_rates.iloc[x]["inflation"]/100)-1)*100)
        yearly_infl.append(inflation_rates.iloc[x]["inflation"])
    for x, elem in enumerate(cumulative_infl):
        cumulative_infl[x] = round(elem, 2)
    years = [2021-x for x in range(row_nbr, -1, -1)]
    total_inflation = cumulative_infl[-1]

    return cumulative_infl, years, total_inflation, yearly_infl