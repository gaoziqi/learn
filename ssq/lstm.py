import os
import sys
import pandas as pd
import numpy as np
from keras.models import Sequential, model_from_json
from keras.layers import Dense, LSTM, Dropout
from keras.callbacks import TensorBoard


period = 3 if len(sys.argv) < 2 else int(sys.argv[1])
epochs = 300 if len(sys.argv) < 3 else int(sys.argv[2])


def build(period):
    model = Sequential()
    model.add(LSTM(64, return_sequences=True, input_shape=(period, 49)))
    model.add(LSTM(64))
    model.add(Dense(49))
    return model

def one_hot(p):
    res = np.zeros(49, dtype='int32')
    for i in range(6):
        res[p[i]] = 1
    res[32 + p[6]] = 1
    return res

def one_hot_array(a):
    res = []
    for i in a:
        res.append(one_hot(i))
    return res

def get(a, step):
    x = []
    y = []
    for i in range(len(a) - step):
        x.append(one_hot_array(a[i:i + step]))
        y.append(one_hot(a[i + step]))
    return np.array(x), np.array(y)


def shuffle(x, y):
    if x.shape[0] != y.shape[0]:
        print("ERROR MUST BE EQUEL")
    index = np.arange(x.shape[0])
    np.random.shuffle(index)
    x1 = []
    y1 = []
    for i in index:
        x1.append(x[i])
        y1.append(y[i])
    return np.array(x1), np.array(y1)


_build = True
if __name__ == '__main__':
    version = 0
    initial_epoch = 0
    r = pd.read_csv('sj.csv', names=['r0', 'r1', 'r2', 'r3', 'r4', 'r5', 'b0'])
    x1, y1 = get(np.array(r), step=period)
    print('begin')
    if _build:
        model = build(period)
    else:
        model = model_from_json(open('predict/model%d.json' % version).read())
        print('load weight')
        model.load_weights('predict/weight%d_%d.h5' % (version, period))
    # model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])
    model.compile(loss='mse', optimizer='adam')
    os.system('rm -rf logs_%d' % period)
    cbks = [TensorBoard(log_dir='logs_%d' % period, write_images=1, histogram_freq=1)]
    print('begin fit')
    model.fit(x1, y1, batch_size=2, initial_epoch=initial_epoch, epochs=initial_epoch + epochs, verbose=1, callbacks=cbks, validation_split=0.1)
    with open('predict/model%d.json' % version, 'w') as w:
        w.write(model.to_json())
    print('save weight')
    model.save_weights('predict/weight%d_%d.h5' % (version, period))
    print('success')
