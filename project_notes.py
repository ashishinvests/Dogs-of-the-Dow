'''symbol = "cvx"

stock = Pinance(symbol)

stock.get_quotes()

print(stock.quotes_data['trailingAnnualDividendRate'])'''

# Sort the stocks by dividend yield from highest to lowest yield. 

# djia_list = ["IBM", "VZ", "XOM","CVX", "KO", "PG","MRK","JPM","CSCO","MMM","CAT","DWDP","INTC","JNJ","MCD","TRV","HD","UTX","WBA","WMT","BA","MSFT","AXP","AAPL","DIS","GS","UNH","NKE","V"]

#VZ = Stock()
#VZ.buy_stock(40)
#VZ.sell_stock(20)
	
#print(VZ.position)


def buyStocks(stockLibrary, amount):
	for stock in stockLibrary.keys():
		stockLibrary[stock].buy_stock(amount)

stockLibrary = run()



#print(AshishM_TradingAccount.balance)

'''class Portfolio():
	def populate_stocks(list_of_symbols):
		stocks = []
		for each_symbol in list_of_symbols:
			stocks.append(Stock(symbol))
			self.stocks = stocks

my_portfolio = Portfolio()

my_portfolio.populate_stocks(dogs_of_dow)'''