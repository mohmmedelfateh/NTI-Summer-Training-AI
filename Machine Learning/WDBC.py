import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error

# loading and Preparing data
df = pd.read_csv('WDBC.csv')
df['5'].fillna(df['5'].mean(), inplace=True)
x = df.iloc[:, 1: 10].values
y = df.iloc[:, 10].values


# split data to train and test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=False)

# use Decision Tree Classifier model for training
classifier = DecisionTreeClassifier()
classifier.fit(x_train, y_train)

# evaluate the model
y_predict = classifier.predict(x_test)
con = confusion_matrix(y_predict, y_test)
print('confusion_matrix: \n', con)
print('accuracy_score: \n', accuracy_score(y_test, y_predict))
print('mean_squared_error: \n', mean_squared_error(y_test, y_predict))
