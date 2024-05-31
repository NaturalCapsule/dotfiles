import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import cross_val_score, KFold

dataset = pd.read_csv('emails.csv')

corpus = []

for i in range(5700):
    review = re.sub('[^a-zA-Z]', ' ', dataset.iloc[:, 0][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    all_stopwords = stopwords.words('english')
    all_stopwords.append('subject')
    review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
    review = ' '.join(review)
    corpus.append(review)


cv = CountVectorizer(max_features = 5700)
x = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:5700, -1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

knn = KNeighborsClassifier(n_jobs = 100, n_neighbors = 5)
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)

