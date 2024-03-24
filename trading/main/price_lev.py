def level_up(level_price, predict_price):
    price_movie=[]
    for price in level_price:
        if int(str(price)[:2])==int(str(predict_price)[:2]) and ((price>predict_price) or (price<predict_price)):
            price_movie.append(price)
        elif (len(price_movie)<4) and (int(str(price+10)[:2])==int(str(predict_price)[:2]) and ((price>predict_price) or (price<predict_price))):
            price_movie.append(price)

    price_movie.append(predict_price)
    price_movie.sort()
    return price_movie
#научится троить по данным y и прибавлять к x 1 и достраивать график 



            
    