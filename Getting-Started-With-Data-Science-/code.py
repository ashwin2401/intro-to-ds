# --------------
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Read the data
data = pd.read_csv('https://storage.googleapis.com/ga-codeblock-live-prod-live-data/account/b21/2a7f53f8-19f6-45c7-9d74-560da9338b1a/b56/894b4c34-996b-4508-92cd-2407ac5bd182/file.csv')

# print the first 5 rows of the dataset
print(data.head())

# Split the data into independent and target variable
X = data.drop('G3',1)
y = data.G3

# Split the data into train and test data sets
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3)


# --------------
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

# Assign the Randomforrest classifier to a variable rf
rf = RandomForestClassifier()
# Train the model
rf.fit(X_train,y_train)
# Predict the class on the test data
y_pred = rf.predict(X_test)


# --------------
from sklearn.metrics import accuracy_score,mean_absolute_error

# Accuracy score
accuracy_score(y_test,y_pred)


