from scrape_data import read_data

report_2021=r"Data/2a71-das-wage2021opendata-esdc-all-19nov2021-vf.csv"
report_2020=r"useb-dgcelmic-cimtdma-dmawages2020load-fileopen-data2a71-das-wage2020opendata-esdc-all-09dec2020.csv"
report_2019=r"hrdc-drhc.netnc_common-communseb-dgcelmic-cimtdma-dmawages2019load-fileopen-data2a71-das-wage201.csv"
yearly_reports=[report_2019, report_2020, report_2021]

job= input(str("Please enter your job:"))
location=input(str("Please enter your location:"))

def wage_growth(yearly_reports, job):
    data_per_year={}
    for report in yearly_reports:
        median_salary=read_data(report, job, location)[2]
        data_per_year[report]=median_salary
    
    if data_per_year[report_2021]>data_per_year[report_2019]:
        action= "grew"
    else:
        action="dropped"
    percentage= abs((data_per_year[report_2021]-data_per_year[report_2019])/data_per_year[report_2019])
    print("The job salary for "+ job+ " "+ action+ " "+ percentage+ " percent from 2019 to 2021.")
    return data_per_year
