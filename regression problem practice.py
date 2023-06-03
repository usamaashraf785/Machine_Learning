import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("/home/choudhary/Desktop/Usama_Projects/ML-Learning/insurance.csv")

# print(df.head())
# print(df.tail())

df['bmi'] = df['bmi'].replace(0,df['bmi'].mean())
df['age'] = df['age'].replace(0,df['age'].mean())
df['expenses'] = df['expenses'].replace(0,df['expenses'].mean())
# Converting to Binary
# df['sex'] = df['sex'].replace({'male':1, 'female':0})
# df['smoker'] = df['smoker'].replace({'yes':1, 'no':0})
# df['region'] = df['region'].replace({'southeast':1, 'southwest':2, 'northeast':3,'northwest':4})
encoder = LabelEncoder()
df['sex'] = encoder.fit_transform(df['sex'])
df['region'] = encoder.fit_transform(df['region'])
df['smoker'] = encoder.fit_transform(df['smoker'])
print(df)


x=df.drop('expenses', axis=1)
y=df['expenses']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.4)
print(len(x_train))
print(len(y_train))
print(len(x_test))
print(len(y_test))


# Random Forrest Regressor
rf_regressor = RandomForestRegressor(n_estimators=300)
rf_regressor.fit(x_train,y_train)
rf_pred = rf_regressor.predict(x_test)
print("Random Forest Regressor's Mean Square Error: ",np.sqrt(mean_squared_error(y_test,rf_pred)))
print("Random Forest Regressor's Mean absolute Error: ",(mean_absolute_error(y_test,rf_pred)))


# Support Vector Regressor
svm_regressor = SVR()
svm_regressor.fit(x_train,y_train)
svr_pred = svm_regressor.predict(x_test)
print("SVM Regressor's Mean Square Error: ",np.sqrt(mean_squared_error(y_test,svr_pred)))
print("SVM Regressor's Mean absolute Error: ",(mean_absolute_error(y_test,svr_pred)))


# Linear Regression
linear_reg = LinearRegression()
linear_reg.fit(x_train,y_train)
lr_pred = linear_reg.predict(x_test)
print("Linear-Regression's Mean Square Error: ",np.sqrt(mean_squared_error(y_test,lr_pred)))
print("Linear-Regression's Mean absolute Error: ",(mean_absolute_error(y_test,lr_pred)))




# Extract data from webs directly by web scrapping
# Custom logic building karni hai
# Loop work for the range of one year in csv day by day for 365 days
# append in one file
# if else

