from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
from sklearn.model_selection import train_test_split


# loading and Preparing data
df = pd.read_csv('WDBC.csv')
df['5'].fillna(df['5'].mean(), inplace=True)
x = df.iloc[:, 1: 10].values
y = df.iloc[:, 10].values

# split data to train and test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=False)

# Build our ANN model
model = Sequential()
model.add(Dense(12, input_shape=(9,), activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=30, batch_size=20)

# evaluate the model
scores = model.evaluate(x_test, y_test)
print(f"Test {model.metrics_names[1]}: { scores[1] * 100}")

