import numpy as np
import os
import matplotlib.pyplot as plt
import keras
from PIL import Image
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.layers. normalization import BatchNormalization

day_dir = os.listdir('./Data/Train')

# One-Hot Encoding to the Labels
def label_img(str_lab):
    if str_lab == 'Sunday': return np.array([1, 0, 0, 0, 0, 0, 0])
    elif str_lab == 'Monday': return np.array([0, 1, 0, 0, 0, 0, 0])
    elif str_lab == 'Tuesday': return np.array([0, 0, 1, 0, 0, 0, 0])
    elif str_lab == 'Wednesday': return np.array([0, 0, 0, 1, 0, 0, 0])
    elif str_lab == 'Thursday': return np.array([0, 0, 0, 0, 1, 0, 0])
    elif str_lab == 'Friday': return np.array([0, 0, 0, 0, 0, 1, 0])
    elif str_lab == 'Saturday': return np.array([0, 0, 0, 0, 0, 0, 1])

def load_training_data():
    train_data = []
    for folder in day_dir:
        for file in os.listdir('./Data/Train/' + folder):
            label = folder[4:]
            label = label_img(label)
            img = Image.open('./Data/Train/'+ folder + '/' + file)
            img = img.resize((500, 500), 3)
            train_data.append([np.array(img), label])

    return train_data

def load_test_data():
    test_data = []
    for file in os.listdir('./Data/Test'):
        img = Image.open('./Data/Test/' + file)
        img = img.resize((500, 500), 3)
        test_data.append(np.array(img))
    return test_data

train_data = load_training_data()
train_images = np.array([i[0] for i in train_data]).reshape(-1, 500, 500, 3)
train_labels = np.array([i[1] for i in train_data])

model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(500, 500, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(BatchNormalization())
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(BatchNormalization())
model.add(Conv2D(96, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(BatchNormalization())
model.add(Conv2D(96, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(BatchNormalization())
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(BatchNormalization())
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(128, activation='relu'))
model.add(Dense(7, activation = 'softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics = ['accuracy'])
model.fit(train_images, train_labels, batch_size = 50, epochs = 5, verbose = 1)

model.save('model.h5')

# Testing here
test_data = load_test_data()
test_images = np.array([i for i in test_data]).reshape(-1, 500, 500, 3)

label_arr = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
i = 6
plt.imshow(test_images[i])
result = model.predict(test_images[i].reshape(-1, 500, 500, 3))[0]
print(np.max(result))
print('This flower is for', label_arr[np.argmax(result)])
