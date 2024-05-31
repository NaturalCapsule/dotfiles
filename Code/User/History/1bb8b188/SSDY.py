import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor

dataset = pd.read_csv('Housing.csv')
x = dataset.iloc[:, 1:].values
y = dataset.iloc[:, 0].values

ct = ColumnTransformer([('encoder', OneHotEncoder(), [4, 5, 6, 7, 8, 10, 11])], remainder = 'passthrough')
x = ct.fit_transform(x)

si = SimpleImputer(missing_values = np.nan, strategy = 'mean')
x = si.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)

reg = LinearRegression()
reg = 
reg.fit(x_train, y_train)
y_pred = reg.predict(x_test)

print(r2_score(y_test, y_pred))