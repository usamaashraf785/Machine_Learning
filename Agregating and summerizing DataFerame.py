import pandas as pd


data = pd.read_csv('/home/choudhary/Desktop/Usama_Projects/ML-Learning/AggregatingandSummarizing-200324-003230/Aggregation in Python/big_mart_sales.csv')
sum = data.Item_MRP.sum()
print(sum)
mean = data.Item_MRP.mean()
print(mean)
median = data.Item_MRP.median()
print(median)
print(data.columns)
mode = data.Outlet_Type.mode()
# print(mode)
mode = data.Outlet_Type.value_counts()
print(mode)
des = data.describe()
print(des)

d = data.groupby(['Outlet_Size','Item_Type'])
# print(d.first())
print(d.mean())
# print(d.median())
# print(d.sum())
# print(d.max())
# d1 = d['Item_MRP']
print(d)

pivot = pd.pivot_table(data, index='Item_Type', values='Item_Outlet_Sales', aggfunc= 'mean')
print(pivot)

cross = pd.crosstab(data['Outlet_Size'],data['Item_Type'])
print(cross)





