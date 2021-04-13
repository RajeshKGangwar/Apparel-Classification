import numpy as np
from itertools import chain
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing import image
from keras.models import load_model
import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow.python.util import deprecation
deprecation._PRINT_DEPRECATION_WARNINGS = False
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
import cv2


class FashionClassification:
    def __init__(self):

        self.classes = ['Goggles','Hat','Jacket','Shirt','Shoes','Shorts','T-Shirt','Trouser','Wallet','Watch']
        self.model = load_model("models/fashion.h5")



    def FashionPredict(self,img):
        img = cv2.imread(img)
        dim = (224,224)
        resize_img = cv2.resize(img,dim, interpolation = cv2.INTER_AREA)
        array_img = image.img_to_array(resize_img)
        x = np.expand_dims(array_img, axis=0)
        x = preprocess_input(x)
        preds = self.model.predict(x)
        print(preds)
        preds_unlist = list(chain(*preds))
        print(preds_unlist)
        preds_int = [int((round(i, 2))) for i in preds_unlist]
        print(preds_int)
        # self.final_pred_unused = dict(zip(self.class_names,self.preds_int))
        final_pred = dict(zip(self.classes, preds_int))
        # finale = final_pred[1]
        print(100 * '-')
        print(final_pred)
        return final_pred
