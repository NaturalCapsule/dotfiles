import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer

dataset = pd.read_csv('Clean_Dataset.csv')
x = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

le = LabelEncoder()
y = le.fit_transform(y)

ct = ColumnTransformer([('encoder', OneHotEncoder(), [0, 1, 2, 3, 4, 5, 6, 7])], remainder = 'passthrough')
x = ct.fit_transform(x).toarray()
print(x)
