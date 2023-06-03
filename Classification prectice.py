import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

def fix_data(df):
    df['Dependents'] = df['Dependents'].fillna(value=df['Dependents'].mode()[0])

    df['Gender'] = df['Gender'].fillna(value=df['Gender'].mode()[0])

    df['LoanAmount'] = df['LoanAmount'].fillna(value=df['LoanAmount'].mean())

    df['Loan_Amount_Term'] = df['Loan_Amount_Term'].fillna(value=df['Loan_Amount_Term'].median())

    df['Credit_History'] = df['Credit_History'].fillna(value=df['Credit_History'].median())

    df['Self_Employed'] = df['Self_Employed'].fillna(value=df['Self_Employed'].mode()[0])

    df['Married'] = df['Married'].fillna(value=df['Married'].mode()[0])
    return df


def convert_to_binary(df):
    df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0}).astype(int)

    df['Married'] = df['Married'].map({'Yes': 1, 'No': 0}).astype(int)

    df['Dependents'] = df['Dependents'].map({'0': 0, '1': 1, '2': 2, '3+': 3}).astype(int)

    df['Education'] = df['Education'].map({'Graduate': 1, 'Not Graduate': 0}).astype(int)

    df['Self_Employed'] = df['Self_Employed'].map({'Yes': 1, 'No': 0}).astype(int)

    df['Property_Area'] = df['Property_Area'].map({'Urban': 0, 'Rural': 1, 'Semiurban': 2}).astype(int)
    return df

# Reading CSV Files
train = pd.read_csv("/home/choudhary/Desktop/Usama_Projects/ML-Learning/archive/train_u6lujuX_CVtuZ9i.csv")
test = pd.read_csv("/home/choudhary/Desktop/Usama_Projects/ML-Learning/archive/test_Y3wMUE5_7gLdaTN.csv")

# first five values
print(train.head())

# last five values
print(train.tail())

# dataframe info
print(train.info())

# checking null values
print(train.isnull().sum())

# Fixed null values using fix_data function
train = fix_data(train)
test = fix_data(test)
# Converting data to binary using convert_to_binary function
train = convert_to_binary(train)
test = convert_to_binary(test)



x_train = train.drop(['Loan_Status','Loan_ID'],axis=1)
y_train = train['Loan_Status']
# x_train,x_test,y_train,y_test=train_test_split(x,y ,test_size=0.20,random_state=13)

x_test = test.drop(['Loan_ID'],axis=1)

# y_test =
# Simple Classifier
Knn_classifier=KNeighborsClassifier()
Knn_classifier.fit(x_train,y_train)
result=Knn_classifier.predict(x_test)
print(accuracy_score(test,result))


# # Simple Regressor
# lr_regressor = LogisticRegression(C=1.0,penalty='l2',solver='liblinear', random_state=0)
# lr_regressor.fit(x_train,y_train)
# y_pred=lr_regressor.predict(x_test)
# print(accuracy_score(x_test,y_pred))


# RF_classifier = RandomForestClassifier()
# RF_classifier.fit(x_train,y_train)
# y_pred = RF_classifier.predict(x_test)
# print(accuracy_score(x_test,y_pred))

