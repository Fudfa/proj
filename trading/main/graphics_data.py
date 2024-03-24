def grph_data():
    import json
    prices={'open':[],
        'close':[],
        'high':[],
        'low':[],
        'value':[],
    }
    
    with open('prices.json','r') as f:
        s=json.load(f)
    for u in s:
            try:
                prices['open'].append(u['open'])
                prices['close'].append(u['close'])
                prices['high'].append(u['high'])
                prices['low'].append(u['low'])
                prices['value'].append(u['value'])
            except TypeError:
                continue

    with open('graphics.json','w') as f:
            json.dump(prices,f)
    

