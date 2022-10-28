import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from ColumnTrans import ColumnTransAll

# loading and Preparing data
df = pd.read_csv('Data.csv')
x = df.iloc[:, 1:20]
y = df.iloc[:, -1]
le = LabelEncoder()
y = le.fit_transform(y)
y = y.ravel()
x = ColumnTransAll(x)

# split data to train and test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, shuffle=False)


# use Random Forest Classifier
classifier_rf = RandomForestClassifier(random_state=42, n_jobs=-1, max_depth=5, n_estimators=100, oob_score=True)
classifier_rf.fit(x_train, y_train)

# evaluate the model
y_predict = classifier_rf.predict(x_test)
con = confusion_matrix(y_predict, y_test)
print('confusion_matrix: \n', con)
print('accuracy_score: \n', accuracy_score(y_test, y_predict))
print('mean_squared_error: \n', mean_squared_error(y_test, y_predict))
