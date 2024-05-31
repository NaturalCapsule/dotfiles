import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

dataset = pd.read_csv('creditcard.csv')
x = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values
print(x)
print(y)