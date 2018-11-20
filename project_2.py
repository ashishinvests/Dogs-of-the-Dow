
# Code to get djia symbol list
from pinance import Pinance
import bs4 as bs
import pickle
import requests

def save_djia_tickers():
	resp = requests.get("http://www.dogsofthedow.com/ddoggish.htm")	
	soup = bs.BeautifulSoup(resp.text)
	table = soup.find("table", {"class" : "xl166924767"})
	tickers = []
	for row in table.findALL('tr')[1:]:
		ticker = row.findAll('td')[1].text.replace('.','-')
		tickers.append(ticker)

	with open("djiatickers.pickle", "wb") as f:
		pickle.dump(tickers, f)


	print(tickers)	
	return(tickers)

save_djia_tickers()




#link to get djia symbol list "https://pythonprogramming.net/sp500-company-list-python-programming-for-finance/"