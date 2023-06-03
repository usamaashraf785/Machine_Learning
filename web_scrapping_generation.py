import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import csv
from datetime import timedelta,datetime


def data():
    start_date = datetime(2015,1,1)
    end_date = datetime(2015, 3, 1)
    timedelta(days=1)
    data = []
    for current_date in range(int((end_date - start_date).days)):
        data.append((start_date + timedelta(current_date)).strftime("%d.%m.%Y"))
    return data


for date_str in data():
    # print(date_str)
    # url = f"https://transparency.entsoe.eu/load-domain/r2/totalLoadR2/show?name=&defaultValue=false&viewType=TABLE&areaType=BZN&atch=false&dateTime.dateTime={date_str}+00:00|CET|DAY&biddingZone.values=CTY|10Y1001A1001A83F!BZN|10Y1001A1001A63L&dateTime.timezone=CET_CEST&dateTime.timezone_input=CET+(UTC+1)+/+CEST+(UTC+2)"
    url = "https://transparency.entsoe.eu/generation/r2/actualGenerationPerGenerationUnit/show?name=&defaultValue=true&viewType=TABLE&areaType=BZN&atch=false&dateTime.dateTime=01.01.2015+00:00|CET|DAYTIMERANGE&dateTime.endDateTime=01.01.2015+00:00|CET|DAYTIMERANGE&area.values=CTY|10Y1001A1001A83F!BZN|10Y1001A1001A63L&masterDataFilterName=&masterDataFilterCode=&productionType.values=B01&productionType.values=B02&productionType.values=B03&productionType.values=B04&productionType.values=B05&productionType.values=B06&productionType.values=B07&productionType.values=B08&productionType.values=B09&productionType.values=B10&productionType.values=B11&productionType.values=B12&productionType.values=B13&productionType.values=B14&productionType.values=B20&productionType.values=B15&productionType.values=B16&productionType.values=B17&productionType.values=B18&productionType.values=B19&dateTime.timezone=CET_CEST&dateTime.timezone_input=CET+(UTC+1)+/+CEST+(UTC+2)&dv-datatable_length=50"
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "lxml")

    table = soup.find("div", class_="table-container")
    # print(table)
    headers = table.find_all('span')
    print(headers)
    # titles = []
    # for i in headers:
    #     title = i.text
    #     if (title == ("Time")):
    #         titles.append(title)
    #     elif (title == 'Day-ahead Total Load Forecast [6.1.B]'):
    #         titles.append(title)
    #     elif (title == 'Actual Total Load [6.1.A]'):
    #         titles.append(title)
    #     else:
    #         pass
    #
    # df = pd.DataFrame(columns=titles)
    #
    # rows = table.find_all('tr')
    # for i in rows[3:]:
    #     # print(i.text)
    #     t_data = i.find_all('td')
    #     t_row = [tr.text for tr in t_data]
    #     # print(t_row)
    #     l = len(df)
    #     df.loc[l] = t_row
    # print(df)
    #
    # file_exists = os.path.isfile('entsoe_load.csv')
    #
    # # Append DataFrame to the CSV file
    # with open('entsoe_load.csv', 'a', newline='') as file:
    #     df.to_csv(file, index=False, header=not file_exists)
