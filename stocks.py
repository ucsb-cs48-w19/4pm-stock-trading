from flask import Flask, render_template, request
from iexfinance.stocks import Stock
from urllib.request import urlopen

#class Stock:                                                                                                                                                                                               
#   def __init__(self,name):                                                                                                                                                                                
#       self.price =                                                                                                                                                                                        
#       self.name  = name                                                                                                                                                                                   




Tesla = Stock("TSLA")
Apple = Stock("AAPL")
Google = Stock("GOOGL")
Microsoft = Stock("MSFT")
Amazon = Stock("AMZN")


#print(Stock1.name)                                                                                                                                                                                         

def getChart(name):
    json = urlopen("https://api.iextrading.com/1.0/stock/"+ name + "/chart/1y").read()
    return json


