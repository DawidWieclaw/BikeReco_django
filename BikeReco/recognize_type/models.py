from django.db import models

# Create your models here.

from django.contrib.auth.models import User
import cv2
from tensorflow import keras
import numpy as np


class NNModel():
    def __init__(self):
        self.resnet_model = keras.models.load_model('../resnet_model')
        self.resnet_model.compile(optimizer=keras.optimizers.Adam(0.001),loss='categorical_crossentropy',metrics=['accuracy'])

    def predict(self, img):

        resized = cv2.resize(np.asarray(img), (160,160))
        print(resized.shape)
        pred = self.resnet_model.predict(resized.reshape((1, 160, 160, 3))).argmax()
        return pred

class Recognizer(models.Model):
    #image=models.ImageField('images/')

    def __str__(self):
        return ""
