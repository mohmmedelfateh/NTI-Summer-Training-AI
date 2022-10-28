import random
import numpy as np
import cv2
import os
import tensorflow as tf
from keras import Sequential
from keras.layers import Conv2D, MaxPool2D, Flatten, Dense, Dropout

# loading and Preparing training data
datadir = r"C:\Users\mmmzz\OneDrive\سطح المكتب\NTI\Datasets\Skin Cancer\train"
categories = ['benign', 'malignant']
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

# Regularization is a technique to reduce the complexity of the model
# Use Regularization to avoid OverFitting
tf.keras.regularizers.L2(l2=0.01)
model = Sequential()
model.add(Conv2D(filters=64, kernel_size=5, strides=(2, 2), padding='same', input_shape=(ImgSize, ImgSize, 3)))
model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2), padding="valid"))
# model.add(Dropout(0.1))
model.add(Flatten())
model.add(Dense(256, activation="relu"))
model.add(Dense(128, activation="relu"))
model.add(Dense(64, activation="relu"))
model.add(Dense(32, activation="relu"))
model.add(Dense(1, activation="sigmoid", kernel_regularizer='L2'))

# Compiling model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics='accuracy')

# Fitting model on training data
model.fit(x, y, epochs=7, batch_size=20)


# loading and Preparing testing data
datadir_test = r"C:\Users\mmmzz\OneDrive\سطح المكتب\NTI\Datasets\Skin Cancer\test"
categories_test = ["benign", "malignant"]
testing_data = []
for category in categories_test:
    path_test = os.path.join(datadir_test, category)
    class_num_test = categories_test.index(category)
    for img in os.listdir(path_test):
        try:
            img_array_test = cv2.imread(os.path.join(path_test, img))
            new_array_test = cv2.resize(img_array_test, (ImgSize, ImgSize))
            testing_data.append([new_array_test, class_num_test])
        except Exception as et:
            pass

random.shuffle(testing_data)
x_test = []
y_test = []
for features, labels in testing_data:
    x_test.append(features)
    y_test.append(labels)

x_test = np.array(x_test).reshape(-1, ImgSize, ImgSize, 3)
y_test = np.array(y_test)


# evaluate the model
score = model.evaluate(x_test, y_test)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

# save model after training
model.save("Skin_Cancer.h5")
