import bs4 as bs
import stocks
import pickle
import requests
import json

def save_stock_tickers(names, tickers, prices):
	resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
	soup = bs.BeautifulSoup(resp.text, 'lxml')
	table = soup.find('table', {'class': 'wikitable sortable'})
	#stockDict = {}
	for row in table.findAll('tr')[1:]:
		name = row.findAll('td')[0].text
		ticker = row.findAll('td')[1].text
	#	stockDict[ticker] = 0
	#	stockDict[ticker + '-name'] = name
		names.append(name)
		tickers.append(ticker)
	with open("sp500tickers.pickle","wb") as f:
		pickle.dump(tickers,f)
	#file = open('Data/stockData.txt', 'w')
	#file.write(json.dumps(stockDict))
	#file.close()
	return tickers
'''
names = []
tickers = []

save_stock_tickers(names, tickers)

print("NAMES: ------")
print(names)
print("tickers: ------")
print(tickers)'''
