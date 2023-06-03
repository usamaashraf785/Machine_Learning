import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import csv
from datetime import timedelta,datetime


def data():
    start_date = datetime(2015,1,1)
    end_date = datetime(2015, 1, 2)
    timedelta(days=1)
    data = []
    for current_date in range(int((end_date - start_date).days)):
        data.append((start_date + timedelta(current_date)).strftime("%d.%m.%Y"))
    return data


for date_str in data():
    # print(date_str)
    url = f"https://transparency.entsoe.eu/load-domain/r2/totalLoadR2/show?name=&defaultValue=false&viewType=TABLE&areaType=BZN&atch=false&dateTime.dateTime={date_str}+00:00|CET|DAY&biddingZone.values=CTY|10Y1001A1001A83F!BZN|10Y1001A1001A63L&dateTime.timezone=CET_CEST&dateTime.timezone_input=CET+(UTC+1)+/+CEST+(UTC+2)"
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "lxml")

    table = soup.find("div", class_="table-container")

    headers = table.find_all('span')

    titles = []
    for i in headers:
        title = i.text
        if (title == ("Time")):
            titles.append(title)
        elif (title == 'Day-ahead Total Load Forecast [6.1.B]'):
            titles.append(title)
        elif (title == 'Actual Total Load [6.1.A]'):
            titles.append(title)
        else:
            pass

    df = pd.DataFrame(columns=titles)

    rows = table.find_all('tr')
    print(rows)
    for i in rows[3:]:
        # print(i.text)
        t_data = i.find_all('td')
        t_row = [tr.text for tr in t_data]
        # print(t_row)
    #     l = len(df)
    #     df.loc[l] = t_row
    # print(df)
    #
    # file_exists = os.path.isfile('entsoe_load.csv')
    #
    # # Append DataFrame to the CSV file
    # with open('entsoe_load.csv', 'a', newline='') as file:
    #     df.to_csv(file, index=False, header=not file_exists)
