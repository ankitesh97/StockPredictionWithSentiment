
import pandas as pd
import numpy as np
import json
import requests


def make_data():
    data = json.loads(open('dataGot.json','r').read())
    senti = np.array(pd.read_csv('generatedscores.csv').get(['positive','negative']))
    embeddings = json.loads(open('generatedscores.json','r').read())["l"]
    print embeddings[0]
    y = np.array(data['close'])
    print len(y)
    X_relevant = np.array([[data['vol'][i],data['open'][i],data['low'][i],data['high'][i]] for i in range(len(y))])
    X = []
    max_price = -1
    min_price = 10000
    for i in range(len(X_relevant)-1, -1, -1):
        x_t = []
        x_t.append(X_relevant[i][0])
        x_t.append(X_relevant[i][1])
        x_t.append(X_relevant[i][2])
        x_t.append(X_relevant[i][3])
        max_price = max(y[i], max_price)
        x_t.append(max_price)
        min_price = min(y[i], min_price)
        x_t.append(min_price)
        x_t.append(senti[i][0])
        x_t.append(senti[i][1])
        x_t += embeddings[i]
        X.append(x_t)

    X = np.array(X)
    print X.shape
    X = X.reshape(X.shape[0],1,X.shape[1])
    data = {}
    data["X"] = X.tolist()
    data["y"] = y.tolist()
    json.dump(data,open('data_senti_word.json','w'))

def get_stock_data():
    link = 'https://query1.finance.yahoo.com/v8/finance/chart/GOOG?range=1d&includePrePost=false&interval=2m&corsDomain=in.finance.yahoo.com&.tsrc=finance'
    resp = requests.get(link)
    data = json.loads(resp.text)
    data = data['chart']['result'][0]['indicators']['quote'][0]
    volume = data['volume']
    close = data['close']
    low = data['low']
    high = data['high']
    open_val = data['open']
    json.dump(dict(vol=volume,close=close,low=low,high=high,open=open_val), open('dataGot.json','w'))


make_data()
