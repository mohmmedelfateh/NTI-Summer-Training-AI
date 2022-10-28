import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import PolynomialFeatures

# loading and Preparing data
df = pd.read_csv('salary_predict_dataset.csv')
df['test_score'].fillna(df['test_score'].mean(), inplace=True)
df['interview_score'].fillna(df['interview_score'].mean(), inplace=True)
x = df.drop('Salary', axis=1).values
y = df.iloc[:, 3].values

# Convert features to truth table columns
CT = ColumnTransformer([('first', OneHotEncoder(), [0])], remainder='passthrough')
x = CT.fit_transform(x)

# Choose the appropriate degree
poly_reg = PolynomialFeatures(degree=4)
x_Poly = poly_reg.fit_transform(x)
poly_reg.fit(x_Poly, y)


# split data to train and test and use Linear Regression model for training
x_train, x_test, y_train, y_test = train_test_split(x_Poly, y, test_size=0.1)
reg = linear_model.LinearRegression()
reg.fit(x_train, y_train)

# evaluate the model
print('mean_squared_error: \n', mean_squared_error(y_test, reg.predict(x_test)))

"""
The mean squared error does not really express the error rate here 
because of the large values of the expected and true values
"""
# we can compare in this way because data is small
compare = pd.DataFrame({'predict values': reg.predict(x_test), 'true values': y_test})
print(compare)
