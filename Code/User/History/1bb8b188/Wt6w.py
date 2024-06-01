import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

dataset = pd.read_csv('creditcard.csv')
dataset['Class'] = dataset['Class'].astype(int)
x = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0)

classification = LogisticRegression(C = 10, random_state = 0, max_iter = 284807)
classification.fit(x_train,y_train)
y_pred = classification.predict(x_test)

print(accuracy_score(y_test, y_pred))