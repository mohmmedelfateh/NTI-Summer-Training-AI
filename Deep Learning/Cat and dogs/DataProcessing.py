import os
import random
import cv2
import numpy as np

# Here we define our variables,location data, categories, images size and Training data.
datadir = r"C:\Users\mmmzz\OneDrive\سطح المكتب\NTI\Datasets\Cats and Dogs\PetImages"
categories = ['Dog', 'Cat']
ImgSize = 100
Training_data = []

# Here we store the image in Training_data as list like that [images matrix,categories]
for category in categories:
    path = os.path.join(datadir, category)
    class_num = categories.index(category)
    for img in os.listdir(path):
        try:
            # cv2.IMREAD_GRAYSCALE Convert the image to black and white for reduce runtime
            img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
            new_array = cv2.resize(img_array, (ImgSize, ImgSize))
            Training_data.append([new_array, class_num])
        # We ignore the damaged images so that they do not appear as an error and the code stops.
        except Exception as e:
            pass
# shuffle data so that the pictures of each category are not next to each other
random.shuffle(Training_data)
x = []
y = []
for features, labels in Training_data:
    x.append(features)
    y.append(labels)

x = np.array(x)
x = x.reshape(-1, ImgSize, ImgSize, 1)
y = np.array(y)


