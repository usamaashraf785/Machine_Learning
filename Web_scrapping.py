import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv
from urllib.request import urlopen

url = "https://transparency.entsoe.eu/generation/r2/actualGenerationPerGenerationUnit/show?name=&defaultValue=false&viewType=TABLE&areaType=BZN&atch=false&dateTime.dateTime=06.01.2017+00:00|CET|DAYTIMERANGE&dateTime.endDateTime=06.01.2017+00:00|CET|DAYTIMERANGE&area.values=CTY|10Y1001A1001A83F!BZN|10Y1001A1001A63L&masterDataFilterName=&masterDataFilterCode=&productionType.values=B01&productionType.values=B02&productionType.values=B03&productionType.values=B04&productionType.values=B05&productionType.values=B06&productionType.values=B07&productionType.values=B08&productionType.values=B09&productionType.values=B10&productionType.values=B11&productionType.values=B12&productionType.values=B13&productionType.values=B14&productionType.values=B20&productionType.values=B15&productionType.values=B16&productionType.values=B17&productionType.values=B18&productionType.values=B19&dateTime.timezone=CET_CEST&dateTime.timezone_input=CET+(UTC+1)+/+CEST+(UTC+2)&dv-datatable_length=50"
# print(url)
r = requests.get(url)
# print(r.content)
soup = BeautifulSoup(r.text, "lxml")
# print(soup)
table = soup.find("table", class_="data-view-table dataTable")
print(table)
# headers = table.find_all('thead')
# print(headers)

#
# titles = []
# for i in headers:
#     title = i.text
#     if (title == ("Type") or title == ("Generation Unit") or title == ("Generation") or title == ("Consumption")):
#         titles.append(title)
#     else:
#         pass
# print(titles)
#
# df = pd.DataFrame(columns=titles)
# # print(df)
#
# rows = table.find_all('tr')
# print(rows)
# for i in rows[2:]:
#     print(i.text)
    # t_data = i.find_all('td')
    # t_row = [tr.text for tr in t_data]
    # print(t_row)
#     l = len(df)
#     df.loc[l] = t_row
#
# print(df)
# df.to_csv("entsoe gen.csv")