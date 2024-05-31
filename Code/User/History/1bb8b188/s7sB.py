import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

dataset = pd.read_csv('Housing.csv')
x = dataset.iloc[:, 1:].values
y = dataset.iloc[:, 0].values

ct = ColumnTransformer([('encoder', OneHotEncoder(), [4, 5, 6, 7, 8, 10, 11])], remainder = 'passthrough')
x = ct.fit_transform(x)
print(x)