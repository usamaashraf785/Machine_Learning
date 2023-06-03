import pandas as pd
import glob
# Reading CSV File
data = pd.read_csv("/home/choudhary/Desktop/Usama_Projects/ML-Learning/reading_csv-200323-192251/reading_csv/datasets/big_mart_sales.csv")
data.head(5)
# print(data)
# # data.shape
#
# # Skipping the comments in dataframe
# data_comments = pd.read_csv("/home/choudhary/Desktop/Usama_Projects/ML-Learning/reading_csv-200323-192251/reading_csv/datasets/big_mart_sales_top_row_error.csv", skiprows=5)
# # data_comments.head(6)
# # print(data_comments)

# Reading the more dataframes and concatinating
df_list = []
for dic in glob.glob('/home/choudhary/Desktop/Usama_Projects/ML-Learning/reading_csv-200323-192251/reading_csv/datasets/multi-directory/*'):
    for file in glob.glob(dic+'/*'):
        df_list.append(pd.read_csv(file))
        # print(file)
final_data =  pd.concat(df_list)
final_data.head(5)
print(final_data)
    # print(dic)
#
#
# Read_Sample = pd.read_csv('/home/choudhary/Desktop/Usama_Projects/ML-Learning/reading_csv-200323-192251/reading_csv/datasets/big_mart_sales.csv', nrows=100)
# # print(Read_Sample)
#
#
# read_sp_colms = pd.read_csv('/home/choudhary/Desktop/Usama_Projects/ML-Learning/reading_csv-200323-192251/reading_csv/datasets/big_mart_sales.csv', usecols=['Outlet_Type'])
# print(read_sp_colms)