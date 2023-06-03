import pandas as pd
import json
from pprint import pprint
data = pd.read_json('/home/choudhary/Desktop/Usama_Projects/ML-Learning/reading_json-200323-192414/reading_json/datasets/simple.json')
data.head()
print(data)
#
#
# data_records = pd.read_json('/home/choudhary/Desktop/Usama_Projects/ML-Learning/reading_json-200323-192414/reading_json/datasets/simple_records.json', lines=True)
# data_records.head()
# # print(data_records)


with open('/home/choudhary/Desktop/Usama_Projects/ML-Learning/reading_json-200323-192414/reading_json/datasets/nested.json') as js:
    data_json = json.load(js)
# pprint(data_json)
# print(data_json)


# data_0 = data_json[0]
# data_0
# print(data_0['details'])

# for data in data_json:
    # print(data['details']['age'])

filterd_data = []
for data in data_json:
    filt_var = {}
    if data['details']['age'] > 15:
        filt_var['age'] = data['details']['age']
        filt_var['name'] = data['details']['name']
        filterd_data.append(filt_var)
print(filterd_data)
# print(filterd_data)

with open('/home/choudhary/Desktop/Usama_Projects/ML-Learning/reading_json-200323-192414/reading_json/datasets/filtered_data.json', 'w') as f:
    json.dump(filterd_data,f,indent=4)

filterd_file = pd.read_json('/home/choudhary/Desktop/Usama_Projects/ML-Learning/reading_json-200323-192414/reading_json/datasets/filtered_data.json')
print(filterd_file)


