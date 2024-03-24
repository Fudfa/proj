import matplotlib.pyplot as plt
import json
import pandas as pd
from graphics_data import grph_data
from dates_data import dates_dat
from trend import trends
from prices_data import prs_data
from user_info import info
from levels import levels
from model_short import model_ii


d1=info()
try:
        prs_data(d1[0],d1[1],d1[2])
except TypeError:
        print('''
        инвестор - день неделя месц квартал
        трейдер - минута десять час день
        ''')
        d1=info()
        prs_data(d1[0],d1[1],d1[2])

type1= d1[-1]
dates_dat(type1)

grph_data()
levels(d1[-1])
with open('graphics.json','r') as f:
    s = json.load(f)

with open('dates.json','r') as f1:
    dates=json.load(f1)

y=[i for i in range(0,len(dates))]

stock_prices=pd.DataFrame(s)

up = stock_prices[stock_prices.close >= stock_prices.open]

down = stock_prices[stock_prices.close < stock_prices.open]
col1 = 'green'
col2 = 'red'

width = .73
width2 = .2

plt.bar(up.index, up.close-up.open, width, bottom=up.open, color=col1)
plt.bar(up.index, up.high-up.close, width2, bottom=up.close, color=col1)

plt.bar(up.index, up.low-up.open, width2, bottom=up.open, color=col1)
plt.bar(down.index, down.close-down.open, width, bottom=down.open, color=col2)

plt.bar(down.index, down.high-down.open, width2, bottom=down.open, color=col2)
plt.bar(down.index, down.low-down.close, width2, bottom=down.close, color=col2)

with open('levl_ret.json','r') as f:
        lev = json.load(f)

for levl in lev:
    plt.axhline(y=levl)

keys_tr=[]
trend_line=trends()
for yt in trend_line.keys():
    keys_tr.append(yt)

price_predict=model_ii()
for u in range(len(keys_tr)-1):
    plt.plot([keys_tr[u],keys_tr[u+1]],[trend_line[keys_tr[u]],trend_line[keys_tr[u+1]]])
plt.plot(len(stock_prices.close)+4, price_predict, "ro")
plt.xticks(ticks =y,labels=dates,rotation='vertical')
plt.show()
    
