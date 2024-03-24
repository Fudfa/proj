def pred_pr():
    import json
    from model import model_ii
    prices={'open':[],
        'close':[],
        'high':[],
        'low':[],
        'value':[],
    }
    with open("graphics.json",'r') as f:
        s=json.load(f)

    for i in s.keys():
        f=s[i]
        for u in range(8):
            pred_price = model_ii()
            f.append(pred_price)

        prices[i]=f
    
    with open("gr_pr.json",'w') as f:
        json.dump(prices,f)





    