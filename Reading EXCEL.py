import pandas as pd
import glob

# Reading Excel File
# data = pd.read_excel('/home/choudhary/Desktop/Usama_Projects/ML-Learning/reading_excel-200911-130414/reading_excel/datasets/big_mart_sales.xlsx')
# data.head(5)
# print(data)

# Reading Multiple sheets

data_multy_sheets = pd.read_excel('/home/choudhary/Desktop/Usama_Projects/ML-Learning/reading_excel-200911-130414/reading_excel/datasets/big_mart_sales_with_multiple_sheets.xlsx')
# data_multy_sheets.Item_Weight.unique()
data_multy_sheets.Outlet_Establishment_Year.unique()
data_multy_sheets.head()
# print(data_multy_sheets)

Sheet_1997 = pd.read_excel('/home/choudhary/Desktop/Usama_Projects/ML-Learning/reading_excel-200911-130414/reading_excel/datasets/big_mart_sales_with_multiple_sheets.xlsx', sheet_name='1997')
# print(Sheet_1997)
sheet_1985 = pd.read_excel('/home/choudhary/Desktop/Usama_Projects/ML-Learning/reading_excel-200911-130414/reading_excel/datasets/big_mart_sales_with_multiple_sheets.xlsx', sheet_name='1985')
sheet_1987 = pd.read_excel('/home/choudhary/Desktop/Usama_Projects/ML-Learning/reading_excel-200911-130414/reading_excel/datasets/big_mart_sales_with_multiple_sheets.xlsx', sheet_name='1987')
# print(sheet_)

sheets = pd.concat([Sheet_1997,sheet_1985,sheet_1987])
# print(sheets)

sheet_comment = pd.read_excel('/home/choudhary/Desktop/Usama_Projects/ML-Learning/reading_excel-200911-130414/reading_excel/datasets/big_mart_sales_comments.xlsx', skiprows=3)
# print(sheet_comment)



excel_list = []

for dir in glob.glob('/home/choudhary/Desktop/Usama_Projects/ML-Learning/reading_excel-200911-130414/reading_excel/datasets/multi-directory-excel/*'):
    for file in glob.glob(dir+'/*'):
        excel_list.append(pd.read_excel(file))
print(excel_list)