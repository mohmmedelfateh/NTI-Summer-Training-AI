import keras.utils
from keras import datasets
from keras.layers import Dense, Conv2D, MaxPool2D, Flatten
from keras.models import Sequential
from keras.datasets import cifar10

# load dataset
(x_train, y_train), (x_test, y_test) = datasets.cifar10.load_data()

# transform output to truth table with 10 column
y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

# reshaping data
x_train = x_train.reshape(50000, 32, 32, 3)
x_test = x_test.reshape(10000, 32, 32, 3)

# scaling data
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255

# Build our CNN model
model = Sequential()
model.add(Conv2D(filters=32, kernel_size=5, strides=(1, 1), padding="same", input_shape=(32, 32, 3)))
model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2), padding="valid"))
model.add(Flatten())
model.add(Dense(512, activation="relu"))
model.add(Dense(256, activation="relu"))
model.add(Dense(128, activation="relu"))
model.add(Dense(64, activation="relu"))
model.add(Dense(10, activation="softmax"))


# Compiling model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fitting model on training data
model.fit(x_train, y_train, epochs=10, batch_size=40)

# evaluate the model
scores = model.evaluate(x_test, y_test)
print(f"Test {model.metrics_names[1]}: { scores[1] * 100}")

# save model after training
model.save("Cifar10_dataset.h5")
