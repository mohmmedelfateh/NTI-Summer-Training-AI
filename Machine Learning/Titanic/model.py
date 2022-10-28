import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import linear_model

# loading and Preparing training data
df = pd.read_csv('train.csv')
df['Age'].fillna(int(df['Age'].mean()), inplace=True)
y_train = df.iloc[:, 1].values
x_train = df.iloc[:, [2, 4, 5, 9]].values


# loading and Preparing training data
df2 = pd.read_csv('test.csv')
df2['Age'].fillna(int(df['Age'].mean()), inplace=True)
y_test = df.iloc[:, 1].values
x_test = df.iloc[:, [2, 4, 5, 9]].values

# convert string in column to number
# ["tokyo", "tokyo", "paris"] to [2, 2, 1]
label = LabelEncoder()
x_train[:, 1] = label.fit_transform(x_train[:, 1])
x_test[:, 1] = label.fit_transform(x_test[:, 1])

# use Decision Tree Classifier model for training
reg = DecisionTreeClassifier()
reg.fit(x_train, y_train)

# evaluate the model
y_pre = reg.predict(x_test)
print('DecisionTreeClassifier: ')
print('mean_squared_error: ', mean_squared_error(y_test, y_pre))
con = confusion_matrix(y_pre, y_test)
print('confusion_matrix: \n', con, "\n")


# use Logistic Regression model for training
reg = linear_model.LogisticRegression()
reg.fit(x_train, y_train)

# evaluate the model
y_pre_log = reg.predict(x_test)
print('LogisticRegression: ')
print('mean_squared_error: ', mean_squared_error(y_pre_log, y_test))
con_log = confusion_matrix(y_pre_log, y_test)
print('confusion_matrix: \n', con_log)


