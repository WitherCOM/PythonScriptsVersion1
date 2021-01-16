import cv2
import numpy as np

from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten
X_train = np.empty((16,109,112,3))
y_train = np.array(['muffin','dog','muffin','dog','dog','muffin','dog','muffin','muffin','dog','muffin','dog','dog','muffin','dog','muffin'])
#load images 
for i in range(1,17):
    img_part = cv2.imread('cookie and dog\\img{}.png'.format(i))
    X_train[i-1] = img_part
model = Sequential()
print(X_train.__len__())
model.add(Conv2D(64, kernel_size=3, activation='relu',input_shape=(109,112,3)))

model.add(Conv2D(32, kernel_size=3,activation='relu'))

model.add(Flatten())

model.add(Dense(10,activation='softmax'))

model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

print(X_train.shape)
print(y_train.shape)

model.fit(X_train,y_train)
