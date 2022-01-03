# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 20:41:13 2021

@author: Collin
"""
#import tensorflow and read dataset
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

#visualize data
import matplotlib.pyplot as plt
image_index = 5
print(y_train[image_index])
plt.imshow(x_train[image_index])
plt.imshow(x_train[image_index], cmap= 'Greys')

#Reshaping the array to 4-dims to work with Keras API
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
input_shape = (28, 28, 1)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# Normalizing the RGB codes by dividing it to the max RGB value
x_train /= 255
x_test /= 255
print(x_train.shape)
print(x_test.shape)

#creating Sequential model with layers
model = Sequential()
model.add(Conv2D(28, kernel_size = (3,3), input_shape = input_shape))