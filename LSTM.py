from keras.models import Sequential
from keras.layers import LSTM, Dense
import numpy as np

data_dim = 16
timesteps = 8
num_classes = 4
batch_size = 32
EPOCHS = 10
num_hidden = 32

# Expected input batch shape: (batch_size, timesteps, data_dim)
# Note that we have to provide the full batch_input_shape since the network is stateful.
# the sample of index i in batch k is the follow-up for the sample i in batch k-1.
model = Sequential()
model.add(LSTM(num_hidden, return_sequences=True, stateful=True,
               batch_input_shape=(batch_size, timesteps, data_dim)))
model.add(LSTM(num_hidden, return_sequences=True, stateful=True))
model.add(LSTM(num_hidden, stateful=True))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

# Generate dummy training data
x_train = np.random.random((2,batch_size * 10, timesteps, data_dim))
y_train = np.random.randint(0,4,(2,batch_size * 10, num_classes))

# Generate dummy validation data
x_val = np.random.random((2,batch_size * 3, timesteps, data_dim))
y_val = np.random.randint(0,4,(2,batch_size * 3, num_classes))

for e in range(1):
    for i in range(x_train.shape[0]):
        model.fit(x_train[i], y_train[i],
                  batch_size=batch_size, epochs=1, shuffle=False,
                  validation_data=(x_val[i], y_val[i]))
        model.reset_states()
        
x_test = np.random.random((1,batch_size*10,8,16))
for j in range(x_test.shape[0]):
    for k in range(x_test.shape[1]/batch_size):
        y_pred = model.predict_on_batch(x_test[j][k:k+batch_size])
    model.reset_states()
    print(y_pred.shape)