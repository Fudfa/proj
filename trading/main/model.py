def model_ii():    
    from tensorflow import keras
    from tensorflow.keras import layers
    import tensorflow as tf
    import matplotlib.pyplot as plt
    import numpy as np
    import os
    import pandas as pd
    from keras.callbacks import EarlyStopping

    if os.path.isfile("model_ii.keras"):
        from model2 import model_ii2
        pred = model_ii2()
        return pred

    fname=os.path.join("prices.json")
    data=pd.read_json(fname)

    split=0.9
    i_split=int(len(data)*split)
    cols=["close","value"]
    data_train=data.get(cols).values[:i_split]
    data_test=data.get(cols).values[i_split:]
    len_train=len(data_train)
    len_test=len(data_test)

    sequence_leght=50
    input_dim=2
    batch_size=32
    epochs =20

    model=tf.keras.Sequential([
        tf.keras.layers.LSTM(100, input_shape=(sequence_leght-1, input_dim), return_sequences=True),#выяснить что такое return_sequences
        tf.keras.layers.Dropout(.2),
        tf.keras.layers.LSTM(100, return_sequences=True),
        tf.keras.layers.LSTM(100, return_sequences=False),
        tf.keras.layers.Dropout(.2),
        tf.keras.layers.Dense(1),
    ])

    model.compile(
        optimizer='adam',
        loss='mse',
        metrics=['accuracy']
    )

    def normalise_windows(window_data, single_window=False):
        normalise_data=[]
        window_data= [window_data] if single_window else window_data
        for window in window_data:
            normalise_window=[]
            for col_i in range(window.shape[1]):
                normaalise_col=[((float(p)/ float(window[0, col_i]))-1) for p in window[: , col_i]]
                normalise_window.append(normaalise_col)
            normalise_window=np.array(normalise_window).T
            normalise_data.append(normalise_window)
        return np.array(normalise_data)

    def _next_window(i, seq_len, normalise):
        window = data_train[i:i+seq_len]
        window=normalise_windows(window, single_window=True)[0] if normalise else window
        x=window[:-1]
        y=window[1, [0]]
        return x,y

    def get_train_data(seq_len, normalise):
        data_x=[]
        data_y=[]
        for i in range(len_train-seq_len+1):
            x, y =_next_window(i, seq_len, normalise)
            data_x.append(x)
            data_y.append(y)
        return np.array(data_x), np.array(data_y)

    x,y = get_train_data(
        seq_len=sequence_leght,
        normalise=True,                
    )

    callbacks=[
        EarlyStopping(monitor="loss",patience=2),
        keras.callbacks.ModelCheckpoint(filepath="model_ii.keras")
    ]

    model.fit(x,y,epochs=epochs, batch_size=batch_size, callbacks=callbacks)
    import keras.backend as K
    K.eval(model.optimizer.lr)

    def get_test_data(seq_len, normalise):
        data_window=[]
        for i in range(len_test-seq_len):
            data_window.append(data_test[i:i+seq_len])

        data_window=np.array(data_window).astype(float)
        data_window=normalise_windows(data_window, single_window=False) if normalise else data_window

        x=data_window[:, :-1]
        y=data_window[:, -1, [0]]
        return x,y

    x_test, y_test=get_test_data(
        seq_len=sequence_leght,
        normalise=True,
    )

    model.evaluate(x_test, y_test)
    model.evaluate(x_test, y_test)
    model.evaluate(x_test, y_test)

    def get_last_data(seq_len, normalise):
        last_data=data_test[seq_len:]
        data_windows=np.array(last_data).astype(float)
        data_windows=normalise_windows(data_windows, single_window=True) if normalise else data_windows
        return data_windows

    last_data_predict_prices= get_last_data(-(sequence_leght-1), False)
    last_data_predict_prices_1st_price=last_data_predict_prices[0][0]
    last_2_data=get_last_data(-(sequence_leght-1),True)

    prediction= model.predict(last_2_data)
    print(prediction, prediction[0][0])

    def de_normalise_data(price_1st, _data):
        return (_data+1)*price_1st

    predict_price=de_normalise_data(last_data_predict_prices_1st_price, prediction[0][0])
    return predict_price


