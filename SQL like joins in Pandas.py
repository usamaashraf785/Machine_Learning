import pandas as pd


 # Left Joins in Pandas
student_df = pd.DataFrame({
    'roll_no': [ 102, 101, 104, 103, 105],
    'name' : ['Aravind', 'Rahul', 'Prateek', 'Piyuesh', 'Kartik'],
    'grade': ['B', 'B', 'A', 'C', 'A'],
    'marks': [ 15, 15, 20, 4, 22],
    'city' : ['Gurugram', 'Delhi', 'Delhi', 'Gurugram', 'Hyderabad']
})


# print(student_df)

city_state_mapping = pd.DataFrame({
    'city' :  ['Gurugram', 'Delhi', 'Hyderabad', 'Faridabad'],
    'state' : ['Haryana',  'Delhi', 'Telangana', 'Haryana']
})
print(student_df)

print(student_df.merge(city_state_mapping, how='left', on='city'))



# Right Joins in Pandas
#
# roll_no = pd.DataFrame({
#     'roll_no' : [ 102, 103]
# })
#
# # print(student_df.merge(roll_no, how='right'))
#
#
# #  Outer or Full Joins in Pandas
# student_selection = pd.DataFrame({
#     'roll_no' : [102, 105, 101],
#     'company' : ['ABC', 'XYZ', 'ABC'],
#     'package (lpa)' : [ 8, 14.5, 11 ]
# })
#
#
#
# # print(student_df.merge(student_selection, how='outer'))
#
#
# # Inner Joins in Pandas
#
# student_df = pd.DataFrame({
#     'college': ['ZU UNIVERSITY', 'ZU UNIVERSITY', 'ZU UNIVERSITY', 'ZU UNIVERSITY', 'ZU UNIVERSITY'],
#     'roll_no': [ 102, 101, 104, 103, 105],
#     'name' : ['Aravind', 'Rahul', 'Prateek', 'Piyuesh', 'Kartik'],
#     'grade': ['B', 'B', 'A', 'C', 'A'],
#     'marks': [ 15, 15, 20, 4, 22],
#     'city' : ['Gurugram', 'Delhi', 'Delhi', 'Gurugram', 'Hyderabad']
# })
#
# print(student_df)
# pool = pd.DataFrame({
#         'college': ['ZU UNIVERSITY', 'ZU UNIVERSITY', 'AB UNIVERSITY', 'ZU UNIVERSITY','AB UNIVERSITY'],
#         'name' : ['Aravind', 'Rahul', 'Rahul', 'Prateek', 'Harsh'],
#         'company' : ['ABC', 'XYZ', 'ABC', 'AEP', 'ABC'],
#         'package (lpa)' : [ 8, 14.5, 11, 6, 6 ]
# })
# print(pool)
#
# # print(student_df.merge(pool, how='inner', on=['college','name']))
#
#
#
#










