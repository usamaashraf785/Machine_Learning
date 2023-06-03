import pandas as pd

data1 = pd.read_csv('/home/choudhary/Desktop/Usama_Projects/ML-Learning/Concatenation-200622-144352/Concatenation data/outlet_size_high.csv')

data2 = pd.read_csv('/home/choudhary/Desktop/Usama_Projects/ML-Learning/Concatenation-200622-144352/Concatenation data/outlet_size_medium.csv')

data3 = pd.read_csv('/home/choudhary/Desktop/Usama_Projects/ML-Learning/Concatenation-200622-144352/Concatenation data/outlet_size_small.csv')

final_data = pd.concat([data1,data2,data3], axis=0)

print(final_data)

















