def levels(n):
    import numpy as np
    import json
    from findiff import FinDiff 

    
    with open('prices.json','r') as f:
        s=json.load(f)

    close =[]
    numbers =[]
    levels_ret=[]
    for y in s:
        close.append(y['close'])

    with open('close.json','w') as f:
        json.dump(close,f)

    dx = 1 
    d_dx = FinDiff(0,dx,1)
    clarr = np.asarray(close)
    m1= d_dx(clarr)
    



    limit=0
    while len(numbers)<8:
        limit+=0.00001
        for u in range(len(m1)):
            if n ==1:
                if (m1[u] <limit and m1[u]>0) or (m1[u] >-limit and m1[u]<0):
                    if u in numbers:
                        continue
                    numbers.append(u)
            else:
                if m1[u] ==0:
                    if u in numbers:
                        continue
                    numbers.append(u)
                if (m1[u] <limit and m1[u]>0) or (m1[u] >-limit and m1[u]<0):
                    if u in numbers:
                        continue
                    numbers.append(u)

        

    
    for inf in numbers:
        levels_ret.append(close[inf])

    with open('m1.json','w') as f:
        json.dump(list(m1),f)
        
    with open('levl_ret.json','w') as f:
        json.dump(levels_ret,f)
        
        

