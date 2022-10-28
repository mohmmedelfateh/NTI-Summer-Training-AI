from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


# This function Convert features to truth table columns, eliminating unnecessary columns
def ColumnTransAll(x):
    CT = ColumnTransformer([('first', OneHotEncoder(), [0])], remainder='passthrough')
    x = CT.fit_transform(x)
    x = x[:, 1:]
    CT = ColumnTransformer([('first1', OneHotEncoder(), [2])], remainder='passthrough')
    x = CT.fit_transform(x)
    x = x[:, 1:]
    CT = ColumnTransformer([('first2', OneHotEncoder(), [3])], remainder='passthrough')
    x = CT.fit_transform(x)
    x = x[:, 1:]
    CT = ColumnTransformer([('first3', OneHotEncoder(), [5])], remainder='passthrough')
    x = CT.fit_transform(x)
    x = x[:, 1:]
    CT = ColumnTransformer([('first4', OneHotEncoder(), [7])], remainder='passthrough')
    x = CT.fit_transform(x)
    x = x[:, 1:]
    CT = ColumnTransformer([('first5', OneHotEncoder(), [9])], remainder='passthrough')
    x = CT.fit_transform(x)
    x = x[:, 1:]
    CT = ColumnTransformer([('first6', OneHotEncoder(), [10])], remainder='passthrough')
    x = CT.fit_transform(x)
    x = x[:, 1:]
    CT = ColumnTransformer([('first7', OneHotEncoder(), [12])], remainder='passthrough')
    x = CT.fit_transform(x)
    x = x[:, 1:]
    CT = ColumnTransformer([('first5', OneHotEncoder(), [14])], remainder='passthrough')
    x = CT.fit_transform(x)
    x = x[:, 1:]
    CT = ColumnTransformer([('f5irst', OneHotEncoder(), [16])], remainder='passthrough')
    x = CT.fit_transform(x)
    x = x[:, 1:]
    CT = ColumnTransformer([('fi5rst', OneHotEncoder(), [18])], remainder='passthrough')
    x = CT.fit_transform(x)
    x = x[:, 1:]
    CT = ColumnTransformer([('f4irst', OneHotEncoder(), [20])], remainder='passthrough')
    x = CT.fit_transform(x)
    x = x[:, 1:]
    CT = ColumnTransformer([('fi555rst', OneHotEncoder(), [22])], remainder='passthrough')
    x = CT.fit_transform(x)
    x = x[:, 1:]
    CT = ColumnTransformer([('firs7t', OneHotEncoder(), [24])], remainder='passthrough')
    x = CT.fit_transform(x)
    x = x[:, 1:]
    CT = ColumnTransformer([('first9', OneHotEncoder(), [25])], remainder='passthrough')
    x = CT.fit_transform(x)
    x = x[:, 1:29]
    return x
