import pandas as pd
from sklearn import linear_model
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, PolynomialFeatures

# lode and Preparing data
df = pd.read_csv('insurance.csv')
x = df.iloc[:, 0:6].values
y = df.iloc[:, 6].values

# Convert features to truth table columns, eliminating unnecessary columns
CT = ColumnTransformer([('first', OneHotEncoder(), [1])], remainder='passthrough')
x = CT.fit_transform(x)
x = x[:, 1:]
CT = ColumnTransformer([('first', OneHotEncoder(), [4])], remainder='passthrough')
x = CT.fit_transform(x)
x = x[:, 1:]
CT = ColumnTransformer([('first', OneHotEncoder(), [5])], remainder='passthrough')
x = CT.fit_transform(x)
x = x[:, 1:]

# Choose the appropriate degree
poly_reg = PolynomialFeatures(degree=3)
x_Poly = poly_reg.fit_transform(x)
poly_reg.fit(x_Poly, y)


# split data to train and test and use Linear Regression model for training
x_train, x_test, y_train, y_test = train_test_split(x_Poly, y, test_size=0.1, shuffle=False)
reg = linear_model.LinearRegression()
reg.fit(x_train, y_train)

# evaluate the model
print('mean_squared_error: \n', mean_squared_error(y_test, reg.predict(x_test)))
