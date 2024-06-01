import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer

dataset = pd.read_csv('Clean_Dataset.csv')
print(dataset.info())


ct = ColumnTransformer([('encoder', OneHotEncoder() [])])