def model_ii2():    
    from tensorflow import keras
    from tensorflow.keras import layers
    import tensorflow as tf
    import matplotlib.pyplot as plt
    import numpy as np
    import os
    import pandas as pd
    from keras.callbacks import EarlyStopping
    
    model= keras.models.load_model('model_ii.keras')

    fname=os.path.join("prices.json")
    data=pd.read_json(fname)

    split=0.8
    i_split=int(len(data)*split)
    cols=["close","value"]
    data_test=data.get(cols).values[i_split:]
    len_test=len(data_test)

    sequence_leght=50

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
