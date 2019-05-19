import pickle

# d={'2':'ergferg','5':'erfgrer'}
# with open('history','wb') as fp:
#     H = pickle.dump(d,fp)
with open('/home/prabhakar/Desktop/final/30/history','rb') as fp:
    H = pickle.load(fp)

import matplotlib.pyplot as plt
# H = pickle.load('history','rb')
for keys in H:
    print(keys)

plt.plot(H['loss'])
plt.plot(H['val_loss'])
# plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
