from flask import Flask, render_template, request
from iexfinance.stocks import Stock
from urllib.request import urlopen

import json





Tesla = Stock("TSLA")
Apple = Stock("AAPL")
Google = Stock("GOOGL")
Microsoft = Stock("MSFT")
Amazon = Stock("AMZN")

  

def getChart(name):
    json1 = urlopen("https://api.iextrading.com/1.0/stock/"+ name + "/chart/1y").read()
    j = json.loads(json1) 
    answer = {}
    for dict in j:
        answer[dict['date']] = dict['open']
    return answer

#    s = "{"
 #   for d in j:
 #      s+= d['date'] + ":" + d['open']
       
 #   s += "}"    
 #   return s    

>>>>>>> fef6f3d65879a30aa9f82a0865157654ae913559
