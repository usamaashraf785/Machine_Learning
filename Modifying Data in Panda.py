import pandas as pd


data = pd.read_csv('/home/choudhary/Desktop/Usama_Projects/ML-Learning/reading_csv-200323-192251/reading_csv/datasets/big_mart_sales.csv')

# Missing or null Values
print(data.isna().sum())

print(data.loc[data.Item_Weight.isna() == True])


# Fill the null values by mean of the item_weight

data.loc[(data.Item_Weight.isna() == True), 'Item_Weight'] = data.Item_Weight.mean()
# print(data.loc[(data.Item_Weight.isna() == True), 'Item_Weight'] )
print(data.isna().sum())

# Also
data.loc[(data.Outlet_Size.isna() == True), 'Outlet_Size'] = 'Medium'
print(data.isna().sum())



