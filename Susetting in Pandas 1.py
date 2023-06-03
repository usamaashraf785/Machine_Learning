import random

import pandas as pd

data = pd.read_csv('/home/choudhary/Desktop/Usama_Projects/ML-Learning/reading_csv-200323-192251/reading_csv/datasets/big_mart_sales.csv')

# data.index

# print(data.shape)

print(data.columns)
# print(data.head())

# Creating list of Random Numbers

# random_list = [random.randint(1,8523) for i in range(8523)]

# data.index = random_list
# print(data.head())

# year = data.set_index('Outlet_Establishment_Year', drop=True, inplace=True)

# identifier = data.set_index('Item_Identifier', drop=True, inplace=True)

# print(data.head())
# print(data.index)
# print(data.loc['FDN15'])

# print(data.columns)
# print(data[data['Item_Type'] == 'dairy'])
# print(data.all())

#  SUBSETTING ON THE BASE OF Position



# print(data.head())
#
# print(data.tail(6))
#
# print(data[10:15])
#
# print(data.iloc[[1,2,5,67,9],[1,4,7]])



# SUBSETTING BASED ON LABELS

# data.set_index('Item_Identifier', drop=True, inplace=True )
# # print(data.loc[['DRC01']])
# print(data.loc[['FDA03'],['Item_Weight']])
# print(data.head())
# #
# sample_dataFram = pd.DataFrame({
#     'Name' : ['Ali','Usama','Ashraf','Hamza'],
#     'Age' : [18,24,23,26],
#     'Grade' : ['A', 'C','A','B'],
#     'ID' : ['A001','A002','A003','A004']
#
# })
# sample_dataFram.set_index('ID', drop=True, inplace=True)
# sample_dataFram = sample_dataFram.sort_values(by=['Age'])
# # print(sample_dataFram.loc['A002'])
# # print(sample_dataFram.iloc[1:3])
#
#
# # SUBSETTING ON THE BASE OF VALUES
select_col = ['Item_Fat_Content','Outlet_Identifier']
# year = data[(data.Outlet_Establishment_Year.isin([ 1987,1988]))|(data.Outlet_Size == 'Medium')]
year = data[(data.Outlet_Establishment_Year.isin([ 1987,1988]))][select_col]
print(year)
#

