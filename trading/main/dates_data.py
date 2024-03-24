def dates_dat(n):
    import json
    dates=[]
    with open('prices.json','r') as f:
        s=json.load(f)
    if n ==1:
        for u in s:
            dates.append(u['begin'])
    if n ==0:
        for u in s:
            dates.append(u['begin'][0:10])
    dates.sort()
    with open('dates.json','w') as f:
        json.dump(dates,f)

