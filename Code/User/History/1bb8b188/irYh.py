import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer

dataset = pd.read_csv('Clean_Dataset.csv')
print(dataset.info())
print(dataset['class'].value_counts())


ct = ColumnTransformer([('encoder', OneHotEncoder(), [1, 2, 3, 4, 5 ,6, 7, 8])], remainder = 'passthrough')
dataset = np.array(ct.fit_transform(dataset))
print(dataset.head())