def trends():
    import json
    
    coord={}

    with open('m1.json','r') as f:
        proiz=json.load(f)

    with open('close.json','r') as f:
        close_price=json.load(f)
    k=0
    while len(coord)<11:
        k+=0.1
        for u in proiz:
                if u ==0:
                    coord[proiz.index(u)]=close_price[proiz.index(u)]
                if (u <k and u>0) or (u >-k and u<0):
                    coord[proiz.index(u)]=close_price[proiz.index(u)]

    return coord

    