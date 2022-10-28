import random
import numpy as np
import cv2
import os
import tensorflow as tf
from keras import Sequential
from keras.layers import Conv2D, MaxPool2D, Flatten, Dense, Dropout
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split


# loading and Preparing data
datadir = r"C:\Users\mmmzz\OneDrive\سطح المكتب\NTI\Datasets\Weather\dataset"
categories = ['Cloud', 'Rain', 'Shine', 'Sunrise']
ImgSize = 200
Training_data = []
for category in categories:
    path = os.path.join(datadir, category)
    class_num = categories.index(category)
    for img in os.listdir(path):
        try:
            img_array = cv2.imread(os.path.join(path, img))
            new_array = cv2.resize(img_array, (ImgSize, ImgSize))
            Training_data.append([new_array, class_num])
        except Exception as e:
            pass
random.shuffle(Training_data)
x = []
y = []

for features, labels in Training_data:
    x.append(features)
    y.append(labels)
x = np.array(x)
x = x.reshape(-1, ImgSize, ImgSize, 3)
y = np.array(y)

# split data to train and test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, shuffle=False)

# transform output to truth table with 4 column
y_train = to_categorical(y_train, 4)
y_test = to_categorical(y_test, 4)

# scaling data
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255


# Build our CNN model
tf.keras.regularizers.L2(l2=0.01)
model = Sequential()
model.add(Conv2D(filters=64, kernel_size=5, strides=(2, 2), padding='same', input_shape=(ImgSize, ImgSize, 3)))
model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2), padding="valid"))
model.add(Flatten())
model.add(Dense(256, activation="relu"))
model.add(Dense(128, activation="relu"))
model.add(Dense(64, activation="relu"))
model.add(Dense(32, activation="relu"))
model.add(Dense(4, activation="softmax", kernel_regularizer='L2'))


# Compiling model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics='accuracy')
# Fitting model on training data

model.fit(x_train, y_train, epochs=9, batch_size=10)

# Evaluate the model
score = model.evaluate(x_test, y_test)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

# save model after training
model.save("Weather_Predict.h5")

