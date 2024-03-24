def model_ii():
    import numpy as np
    from sklearn import metrics
    from sklearn import model_selection as modsel
    from sklearn import linear_model
    import matplotlib.pyplot as plt
    plt.style.use('ggplot')
    import json
    from sklearn import preprocessing

    with open('close.json') as f:
        prices =json.load(f)

    split=0.9
    i_split=int(len(prices)*split)

    x_train=prices[:i_split]
    if len(x_train)%2==0:
        pass
    else:
        x_train=x_train[:-1]
    x_train=np.array(x_train)
    x_train=x_train.reshape((int(i_split/2),2))
    y_train=prices[:i_split]  
    if len(y_train)%2==0:
        pass
    else:
        y_train=y_train[:-1]
    y_train=np.array(y_train)
    y_train=y_train.reshape((int(i_split/2),2))
    x_train=preprocessing.normalize(x_train)
    y_train=preprocessing.normalize(y_train)

    linreg = linear_model.LinearRegression()

    linreg.fit(x_train, y_train)

    metrics.mean_squared_error(y_train, linreg.predict(x_train))

    linreg.score(x_train, y_train)

    x_test=prices[i_split:]
    if len(x_test)%2==0:
        pass
    else:
        x_test=x_test[:-1]
    x_test=np.array(x_test)
    x_test=x_test.reshape((int(len(x_test)/2),2))
    y_test=prices[i_split:]  
    if len(y_test)%2==0:
        pass
    else:
        y_test=y_test[:-1]
    y_test=np.array(y_test)
    y_test=y_test.reshape((int(len(y_test)/2),2))

    y_pred = linreg.predict(x_test)
    metrics.mean_squared_error(y_test, y_pred)

    return y_pred[-1][0]

