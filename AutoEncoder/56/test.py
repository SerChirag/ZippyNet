
# coding: utf-8

# In[5]:


from keras.layers import Reshape, LeakyReLU, Input, Dense, Conv2D, Conv2DTranspose
from keras.layers import MaxPooling2D, UpSampling2D, Dropout,Flatten, Activation
from keras.models import Model
from keras import backend as K
from keras.models import load_model
from keras.models import load_model
from keras.optimizers import Adam
import numpy as np
import cv2




# autoencoder = model.
popo = []
sample = cv2.resize(cv2.imread("./celebF/"+"000001.jpg"), (40,40), interpolation = cv2.INTER_AREA).astype(float)
sample /= 255.0
popo.append(sample)
x_sample = np.array(popo)
# y = autoencoder.predict(x_sample)*255


encu = load_model('en.h5')
ye = encu.predict(x_sample)
np.save('bin.npy',ye)
# ye=np.load('bin.npy')
# decu = load_model('de.h5')
# yd = decu.predict(ye)*255
# cv2.imwrite('ttt.jpg',yd)
 
