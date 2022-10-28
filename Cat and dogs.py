# Import The libraries we need and the data after it is prepared.
import tensorflow as tf
from DataProcessing import x, y, ImgSize
from keras import Sequential
from keras.callbacks import EarlyStopping
from keras.layers import Conv2D, MaxPool2D, Flatten, Dense, Dropout
from sklearn.model_selection import train_test_split

# split data to train and test and scaling data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.15, shuffle=False)
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255

# Build our CNN model
model = Sequential()  # Sequential is box we put in it our layers.
model.add(Conv2D(filters=64, kernel_size=5, strides=(1, 1), padding='same', input_shape=(ImgSize, ImgSize, 1)))
model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2), padding="same"))
model.add(Flatten())  # Flatten covert image matrix to vector.
model.add(Dropout(0.2))
model.add(Dense(128, activation="relu"))
model.add(Dense(64, activation="relu"))
model.add(Dense(32, activation="relu"))
model.add(Dense(1, activation="sigmoid"))

# Compiling model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics='accuracy')
callback = EarlyStopping(monitor='accuracy', baseline=0.8, patience=1)
# Fitting model on training data
model.fit(x_train, y_train, epochs=8, batch_size=40)
# evaluate the model
scores = model.evaluate(x_test, y_test)
print(f"Test {model.metrics_names[1]}: { scores[1] * 100}")

