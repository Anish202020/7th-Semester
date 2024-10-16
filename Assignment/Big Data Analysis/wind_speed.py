import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

from keras import metrics
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

df = pd.read_csv("wind-speed.csv")
L = len(df)
print(L)

Y = np.array([df.iloc[:,3]])
plt.plot(Y[0,:])
plt.show(block = False)

X1 = Y[:,0:L-5]
X2 = Y[:,1:L-4]
X3 = Y[:,2:L-3]

X = np.concatenate([X1,X2,X3],axis=0)
X = np.transpose(X)

Y = np.transpose(Y[:,3:L-2])

sc = MinMaxScaler(X)
sc.fit(X)
X = sc.transform(X)

sc1 = MinMaxScaler(Y)
sc1.fit(Y)
Y = sc.transform(Y)

X = np.reshape(X,(X.shape[0],1,X.shape(1)))

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2)

model = Sequential()
model.add(LSTM(10,activation='tanh',input_shape=(1,3) ,recurrent_activation='hard_sigmoid'))

model.add(Dense(1))

model.compile(loss="mean_squared_error",optimizer='rmsprops',metrics=[metrics.mae])

model.fit(X_train,Y_train,epochs=25,verbose=2)

predict = model.predict(X_test)
plt.figure(2)
plt.scatter(Y_test,predict)
plt.show(block = False)


plt.figure(3)
Real = plt.plot(Y_test)
Predict = plt.plot(predict)
plt.legend([Predict,Real],["Predicted Data","Real Data"])
plt.show()
