import pandas as pd
from sklearn import linear_model
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, PolynomialFeatures


# lode and Preparing data
df = pd.read_csv('Dataset.csv')
df = df.drop('Posted On', axis=1)
x = df.drop('Rent', axis=1).values
y = df.iloc[:, 1].values
CT = ColumnTransformer([('first', OneHotEncoder(), [2, 3, 4, 5, 6, 7, 9])], remainder='passthrough')
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
