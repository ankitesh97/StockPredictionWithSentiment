
import json
import numpy as np
import matplotlib.pyplot as plt


data = json.loads(open('data2.json','r').read())
data_normal  = np.array(data['acc']).flatten()

data = json.loads(open('data2-senti2.json','r').read())
data_senti  = np.array(data['acc']).flatten()


data = json.loads(open('data2-senti-word2.json','r').read())
data_senti_word  = np.array(data['acc']).flatten()

epochs = [i for i in range(len(data_normal))]

line_normal,  = plt.plot(epochs, data_normal, 'b', label='Without Sentiment, mae: '+str(round(data_normal[-1])))
line_senti, = plt.plot(epochs, data_senti, 'g', label='With Sentiment, mae: '+str(round(data_senti[-1])))
line_senti_word, = plt.plot(epochs, data_senti_word, 'r', label='Sentiment+Word2Vec, mae: '+str(round(data_senti_word[-1])))

plt.legend(handles=[line_normal, line_senti, line_senti_word])
plt.xlabel('Epochs')
plt.ylabel('Mean Absolute Error')

plt.show()
