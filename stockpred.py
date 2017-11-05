from keras.models import Sequential
from keras.layers import LSTM, Dense, Flatten
import numpy as np
import json
data = json.load(open("data_senti_word.json","rb"))
X_train = np.array(data['X'])
y_train = np.array(data['y']).reshape(-1,1)

epochs = 500
num_hidden = 20
data_dim = 58
batch_size=1
meen = np.mean(X_train.reshape(X_train.shape[0],-1),axis=0)
std = np.std(X_train.reshape(X_train.shape[0],-1),axis=0)
X_train -= meen
X_train /= std


model = Sequential()
model.add(LSTM(num_hidden, return_sequences=True, stateful=True,
               batch_input_shape=(batch_size,1,data_dim)))
model.add(LSTM(num_hidden, return_sequences=True, stateful=True))
model.add(Flatten())
model.add(Dense(1))

model.compile(loss='mse',
              optimizer='rmsprop',
              metrics=['mae'])

# x_train = np.random.rand(64,1,6)
# x_test = np.random.rand(64,1,6)
# y_train = np.random.rand(64,)
# y_test = np.random.rand(64,)
accs = []
for e in range(epochs):
    print("EPOCH: "+str(e))
    history = model.fit(X_train, y_train,
              batch_size=batch_size, epochs=1, shuffle=False)
    accs.append(history.history['mean_absolute_error'])
    model.reset_states()

model.save('lstm-senti-word2.h5')
# for k in range(x_test.shape[0]):
#     y_pred = model.predict(x_test[k].reshape(1,1,-1))
#     print(y_pred)
data["mean"]=meen.tolist()
data["std"]=std.tolist()
data['acc']=accs
json.dump(data,open("data2-senti-word2.json","wb"))
