import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.metrics import r2_score


dataset = pd.read_excel('HousePricePrediction.xlsx')


x = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values


ct = ColumnTransformer([('encoder', OneHotEncoder(), [1, 3, 4, 8])], remainder='passthrough')
x = ct.fit_transform(x)

si = SimpleImputer(missing_values=np.nan, strategy='mean')
y = si.fit_transform(y.reshape(-1, 1))
x = si.fit_transform(x).toarray()
y = y.reshape(-1, 1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)


sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train).ravel()
y_test = sc_y.transform(y_test)

regressor = SVR(kernel = 'linear')
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)

print(r2_score(y_test, y_pred))