
# coding: utf-8

# In[1]:


from keras.layers import Reshape, LeakyReLU, Input, Dense, Conv2D, Conv2DTranspose
from keras.layers import MaxPooling2D, UpSampling2D, Dropout,Flatten, Activation
from keras.models import Model
from keras.utils import plot_model
from keras import backend as K
from keras.models import load_model
from keras.models import load_model
from keras.optimizers import Adam
import numpy as np
import cv2


# In[2]:


x_final = np.load("x_finali.npy")
from keras import backend as K
K.tensorflow_backend._get_available_gpus()
# print(x_final[0][0])


# In[7]:


def Encoder():
    input_img = Input(shape=(40, 40, 3))  # adapt this if using `channels_first` image data format   
    e1 = Conv2D(16, (3, 3), padding='same', name='e1')(input_img)
    act1 = LeakyReLU(alpha=0.3)(e1)
    e6 = MaxPooling2D((2, 2), padding='same', name='e6')(act1)
    drop1 = Dropout(0.25)(e6)
    e7 = Conv2D(32, (3, 3), padding='same', name='e7')(drop1)
    act2 = LeakyReLU(alpha=0.3)(e7)
    e8 = MaxPooling2D((2, 2), padding='same', name='e8')(act2)
#     act3 = LeakyReLU(alpha=0.1)(e8)
    drop2 = Dropout(0.25)(e8)
    e9 = Flatten()(drop2)
    den1 = Dense(800)(e9)
    act4 = LeakyReLU(alpha=0.3)(den1)
    drop3 = Dropout(0.25)(act4)
    den2 = Dense(400)(drop3)
    act5 = LeakyReLU(alpha=0.3)(den2)
    drop4 = Dropout(0.25)(act5)
    den3 = Dense(56)(drop4)
    act6 = LeakyReLU(alpha=0.3)(den3)
    pika = Model(input_img, act6)
    return pika


def Decoder():
    input_img = Input(shape=(56,))  # adapt this if using `channels_first` image data format   
    den1 = Dense(400)(input_img)
    act4 = LeakyReLU(alpha=0.3)(den1)
    drop3 = Dropout(0.25)(act4)
    den2 = Dense(800)(drop3)
    act5 = LeakyReLU(alpha=0.3)(den2)
    drop4 = Dropout(0.25)(act5)
    den3 = Dense(3200)(drop4)
    act6 = LeakyReLU(alpha=0.3)(den3)
    drop5 = Dropout(0.25)(act6)
    r1 = Reshape((10,10,32))(drop5)
    dc1 = Conv2DTranspose(32, (3, 3), padding='same', name='dc1')(r1)
    act7 = LeakyReLU(alpha=0.3)(dc1)
    u1 = UpSampling2D((2, 2))(act7)
    dc2 = Conv2DTranspose(16, (3, 3), padding='same', name='dc2')(u1)
    act8 = LeakyReLU(alpha=0.3)(dc2)
    u2 = UpSampling2D((2, 2))(act8)
#     c1 = Conv2D(3, (1,1))(u2)
    f1 = Flatten()(u2)
    den4 = Dense(4800,activation='sigmoid')(f1)
    drop6 = Dropout(0.25)(den4)
    r2 = Reshape((40,40,3))(drop6)
    chu = Model(input_img, r2)
    return chu

x = Input(shape=(40, 40, 3))
autoencoder = Model(x, Decoder()(Encoder()(x)))
autoencoder.compile(optimizer='adam', loss='mse')
H = autoencoder.fit(x_final,x_final,validation_split=0.10,epochs=300,batch_size=32)
autoencoder.layers[1].save('en.h5')
autoencoder.layers[2].save('de.h5')
autoencoder.save('auto.h5')

plot_model(autoencoder, to_file='model.png')
import pickle

with open('history','wb') as fp:
    pickle.dump(H.history,fp)

# In[8]:


popo = []
sample = cv2.resize(cv2.imread("./celebF/"+"000001.jpg"), (40,40), interpolation = cv2.INTER_AREA).astype(float)
sample /= 255.0
popo.append(sample)
x_sample = np.array(popo)
y = autoencoder.predict(x_sample)*255


# In[9]:


cv2.imwrite("text.jpg",y[0])


# In[11]:


encu = load_model('en.h5')
y = encu.predict(x_sample)


# In[12]:


decu = load_model('de.h5')
yd = decu.predict(y)*255


# In[13]:


cv2.imwrite("hello.jpg",yd[0])

