from flask import Flask, render_template, request
from iexfinance.stocks import Stock
from urllib.request import urlopen
import json
import re


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

def getQuote(name):
	name = re.sub(r'[-]', '.', name)
	print(name)
	json1 = urlopen("https://api.iextrading.com/1.0/stock/"+ name + "/quote").read()
	j = json.loads(json1) 
	return j