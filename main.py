#Imports
import numpy as np
import requests

#Init
DATABASE = [
    ["22-1-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/01-22-2020.csv"],
    ["23-1-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/01-23-2020.csv"],
    ["24-1-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/01-24-2020.csv"],
    ["25-1-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/01-25-2020.csv"],
    ["26-1-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/01-26-2020.csv"],
    ["27-1-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/01-27-2020.csv"],
    ["28-1-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/01-28-2020.csv"],
    ["29-1-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/01-29-2020.csv"],
    ["30-1-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/01-30-2020.csv"],
    ["31-1-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/01-31-2020.csv"],
    ["1-2-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/02-01-2020.csv"],
    ["2-2-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/02-02-2020.csv"],
    ["3-2-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/02-03-2020.csv"],
    ["4-2-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/02-04-2020.csv"],
    ["5-2-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/02-05-2020.csv"],
    ["6-2-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/02-06-2020.csv"],
    ["7-2-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/02-07-2020.csv"],
    ["8-2-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/02-08-2020.csv"],
    ["9-2-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/02-09-2020.csv"],
    ["10-2-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/02-10-2020.csv"],
    ["11-2-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/02-11-2020.csv"],
    ["12-2-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/02-12-2020.csv"],
    ["13-2-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/02-13-2020.csv"],
    ["14-2-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/02-14-2020.csv"],
    ["15-2-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/02-15-2020.csv"],
    ["16-2-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/02-16-2020.csv"],
    ["17-2-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/02-17-2020.csv"],
    ["18-2-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/02-18-2020.csv"],
    ["19-2-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/02-19-2020.csv"],
    ["20-2-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/02-20-2020.csv"],
    ["21-2-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/02-21-2020.csv"],
    ["22-2-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/02-22-2020.csv"],
    ["23-2-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/02-23-2020.csv"],
    ["24-2-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/02-24-2020.csv"],
    ["25-2-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/02-25-2020.csv"],
    ["26-2-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/02-26-2020.csv"],
    ["27-2-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/02-27-2020.csv"],
    ["28-2-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/02-28-2020.csv"],
    ["29-2-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/02-29-2020.csv"],
    ["1-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-01-2020.csv"],
    ["2-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-02-2020.csv"],
    ["3-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-03-2020.csv"],
    ["4-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-04-2020.csv"],
    ["5-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-05-2020.csv"],
    ["6-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-06-2020.csv"],
    ["7-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-07-2020.csv"],
    ["8-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-08-2020.csv"],
    ["9-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-09-2020.csv"],
    ["10-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-10-2020.csv"],
    ["11-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-11-2020.csv"],
    ["12-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-12-2020.csv"],
    ["13-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-13-2020.csv"],
    ["14-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-14-2020.csv"],
    ["15-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-15-2020.csv"],
    ["16-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-16-2020.csv"],
    ["17-3-2020","https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv"]
]

#Main
if __name__ == "__main__":
    #Aquiring and organizing data
    DB = []
    for DATA_SITE in DATABASE:
        r = requests.get(DATA_SITE[1])
        dataString = r.text
        dataList = dataString.split("\n")
        dataKeys = dataList[0].split(",")
        dataSheet = []
        for country in dataList[1:]:
            dataSheet.append(country.split(","))
        parcel = (DATA_SITE[0], dataSheet)
        DB.append(parcel)

print("Done") #Line to enable breakpoints for debug purposes