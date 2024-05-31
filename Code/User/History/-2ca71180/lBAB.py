#Importing necessary libraries.
import numpy as np
import pandas as pd
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import CountVectorizer
import re

# creating the dataset.
dataset = pd.read_csv('emails.csv')

# making an empty list for the cleaned texts.
corpus = []

# cleaning the texts using a for loop to iterate over the dataset and clean every text in the 'text' column and removing the stopwords.
for i in range(5728):
    review = re.sub('[^a-zA-Z]', ' ', dataset.iloc[:, 0][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    all_stopwords = stopwords.words('english')
    all_stopwords.append('subject')
    review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
    review = ' '.join(review)
    corpus.append(review)

# creating the bag of words model (consists of 1s and 0s)
cv = CountVectorizer(max_features = 5700)
x = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:5729, -1].values


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

knn = KNeighborsClassifier(n_jobs = 100, n_neighbors = 5)
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)



print(accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))