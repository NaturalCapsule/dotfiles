#Importing libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.metrics import r2_score
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler

#Loading the dataset and seperating x and y variable 
dataset = pd.read_csv('Housing.csv')
x = dataset.iloc[:, 1:].values
y = dataset.iloc[:, 0].values
y = y.reshape(-1, 1)

#Performing OneHotEncoder to convert non-numeric to numeric values
ct = ColumnTransformer([('encoder', OneHotEncoder(), [4, 5, 6, 7, 8, 10, 11])], remainder = 'passthrough')
x = np.array(ct.fit_transform(x))

#Spliting the data into training set and test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0)

#Feature scaling features for the SVR model (it is neccesery for the SVR model)
sc_x = StandardScaler()
x_train, x_test = sc_x.fit_transform(x_train), sc_x.transform(x_test)
sc_y = StandardScaler()
y_train, y_test = sc_y.fit_transform(y_train).ravel(), sc_y.transform(y_test).ravel()

#Creating the SVR model to predict the House Prices
reg = SVR(C = 5, kernel = 'linear')
reg.fit(x_train, y_train)
y_pred = reg.predict(x_test)

#Evaluating the model (it got 71%)
print(r2_score(y_test, y_pred))