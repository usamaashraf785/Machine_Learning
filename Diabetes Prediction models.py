import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
import warnings
warnings.filterwarnings('ignore')


df = pd.read_csv("/home/choudhary/Desktop/Usama_Projects/ML-Learning/diabetes.csv")

print(df.head())
print(df.tail())

print(df.isnull().sum())
print(df['Glucose'])
df['SkinThickness'] = df['SkinThickness'].replace(0,df['SkinThickness'].median())
df['Glucose'] = df['Glucose'].replace(0,df['Glucose'].mean())
df['Insulin'] = df['Insulin'].replace(0,df['Insulin'].median())
df['BloodPressure'] = df['BloodPressure'].replace(0,df['BloodPressure'].mean())
df['BMI'] = df['BMI'].replace(0,df['BMI'].median())
print(df['Glucose'])
print(df.describe())


x = df.drop(["Outcome"], axis=1)
y = df["Outcome"]

x_train,x_test,y_train,y_test=train_test_split(x,y, test_size=0.4, random_state=100)
print(len(x_train))
print(len(y_train))
print(len(x_test))
print(len(y_test))

# KNN Classifier
Knn_classifier=KNeighborsClassifier()
Knn_classifier.fit(x_train,y_train)
result=Knn_classifier.predict(x_test)
print("knn classifier's Accuracy: ",accuracy_score(y_test,result))


# Logistic Regression Classifier
lr_model = LogisticRegression()
lr_model.fit(x_train, y_train)
lr_pred = lr_model.predict(x_test)
print("Logistic Regression's Accuracy: ", accuracy_score(y_test,lr_pred))


# Decision Tree Classifier
dtree_classifier = DecisionTreeClassifier()
dtree_classifier.fit(x_train,y_train)
dtree_pred = dtree_classifier.predict(x_test)
print("Decision Tree's Accuracy: ", accuracy_score(y_test,dtree_pred))


# SVM Classifier
svm_classifier = SVC()
svm_classifier.fit(x_train,y_train)
svm_pred = svm_classifier.predict(x_test)
print("SVM's Classifier's Accuracy: ",accuracy_score(y_test,svm_pred))


# Naive-Bayes Classifier
nb_classifier = GaussianNB()
nb_classifier.fit(x_train,y_train)
nb_pred = nb_classifier.predict(x_test)
print("Naive-Bayes Classifier's Accuracy: ",accuracy_score(y_test,nb_pred))





