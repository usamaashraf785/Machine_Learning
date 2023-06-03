import pandas as pd

data_frame = pd.DataFrame({
    'roll_no': [ 102, 101, 104, 103, 105],
    'name' : ['Aravind', 'Rahul', 'Prateek', 'Piyuesh', 'Kartik'],
    'grade': ['B', 'B', 'A', 'C', 'A'],
    'marks': [ 15, 15, 20, 4, 22],
    'city' : ['Gurugram', 'Delhi', 'Delhi', 'Gurugram', 'Hyderabad']
})



# df  = data_frame.sort_values(by=['roll_no'])

df = data_frame.sort_values(by=['grade','marks'], ascending=[True,False])
data_frame.reset_index(drop=True, inplace=True)

print(df)














