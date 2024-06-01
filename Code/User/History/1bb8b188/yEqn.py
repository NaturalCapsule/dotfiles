import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.model_selection import cross_val_score
# Load the dataset
dataset = pd.read_csv('creditcard.csv')
dataset['Class'] = dataset['Class'].astype(int)

# Split the data into features (X) and target variable (y)
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Train the model
classification = LogisticRegression(C = 10, random_state=0, max_iter=284807)
classification.fit(X_train, y_train)

# Predict on the test set
y_pred = classification.predict(X_test)

# Model evaluation
scores = cross_val_score(classification, X, y, cv=10, scoring='accuracy')
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
print("ROC AUC Score:", roc_auc)
print("Mean Accuracy:", np.mean(scores))