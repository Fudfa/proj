def prs_data(start,end,interval):
    import requests
    import json
    import apimoex.requests
    s=[]
    a=apimoex.requests.get_market_candles(session=requests.Session(),security="SBER",start=start,end=end,interval=interval)
    for i in a:
        s.append(i)
    

    with open('prices.json','w') as f:
        json.dump(s,f)
    

