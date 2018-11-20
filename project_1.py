# Ashish Manandhar
# Dogs of the dow trading strategy.

# Importing Pinance module
from pinance import Pinance

# Import Flask class from flask library. (Note the upper/lowercase convention.)
from flask import Flask

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)




# Creates a BankAccount class.	
class BankAccount(): 
	def __init__(self):
		self.balance = 0
		self.interest = .00


# Function to deposit cash in the bank account.
	def deposit(self, amount_deposit): 
		if amount_deposit <= 0:
			return False
		else:
			self.balance += amount_deposit
		return self.balance 



# Function to withdraw cash in the bank account.
	def withdraw(self, amount_withdraw): 
		if amount_withdraw <= 0:
			return False
		else:
			self.balance -= self.amount_withdraw
		return self.balance


# Adds interest earned in account balance.
	def accumulate_interest(self): 
		self.balance += self.balance * self.interest
		return self.balance
	


############################################################ Needs
# Transfer funds from BankAccount class to BrokerageAccount  To
	# def transfer_brokerage(self, amount_transfer):
		#self.balance -= amount_transfer                     Be 
############################################################ Created

class BrokerageAcccount(BankAccount):
	def __init__(self):
		super().__init__()
		self.balance = 0
		self.interest = 0

	def accumulate_interest(self):
		self.balance += 0
		return self.balance


	def transfer_brokerage(self, amount_transfer):
		self.balance += amount_transfer




# Creating AshishM's primary bank account.
AshishM_BankAccount = BankAccount()

# Creating AshishM's trading account. 
AshishM_TradingAccount = BrokerageAcccount()



# Funding AshishM's primary bank account and printing the balance. 
AshishM_BankAccount.deposit(40000)
print("\nAshishM's bank account has", AshishM_BankAccount.balance, "dollars.")

# Funding AshishM's trading account and printing the balance.

AshishM_TradingAccount.deposit(20000)
print("\nAshishM's trading account has", AshishM_TradingAccount.balance, "dollars.")



# Amount to be allocated for each stock.
stock_allocation = AshishM_TradingAccount.balance/10
print("\nThe amount to be allocated to invest in each of the dogs of the dow stock is", stock_allocation,"dollars.\n")



dogs_of_dow = ["VZ", "IBM", "XOM", "GE", "CVX", "KO", "PG", "PFE", "MRK", "CSCO"]


#TODO Create a `PinanceClient` class that has functions in it that call the pinance code

# TODO this needs to be a function that takes in a list of stocks and puts the quotes into a dictionay
"""
{'VZ': 
	{
		'stock': ...,
		'quote': ...,
		'market_price': ...
	},
	...
}
"""
for each_symbol in dogs_of_dow:
	stock_list = Pinance(each_symbol)
	symbol = each_symbol
	stock = Pinance(symbol)
	stock.get_quotes()
	

# Gets the price of the list of stocks in djia_list.
	price_stock = stock.quotes_data['regularMarketPrice']

# Gets the trailing annual divident of the list of stocks in djia_list.
	dividend_yield = stock.quotes_data['trailingAnnualDividendRate']

# Prints stock tickers, prices, and dif yields of the list of stocks in djia_list.
	#print(each_symbol, price_stock, dividend_yield)

# Calculate number of shares to buy based on stock allocation and the price of each stock in dog list.
	shares_to_buy = stock_allocation/price_stock

# Advise how many shares of each company to buy at the current price.
	#print("\nBuy", shares_to_buy, "shares of", each_symbol, "at", price_stock, "dollars.\n")


# TODO: Create a function that does this, and then another function that calls that first function in a loop

# Get price of stocks from dogs_of_dow list.
#dog 1 price 
dog1 = dogs_of_dow[0]
print("dog1 is", dog1)
dog1_price = Pinance(dog1)
dog1_price.get_quotes()
dog1price = dog1_price.quotes_data['regularMarketPrice']
print("Price of dog1 is", dog1price,"\n")

#dog 2 price
dog2 = dogs_of_dow[1]
print("dog2 is",dog2)
dog2_price = Pinance(dog2)
dog2_price.get_quotes()
dog2price = dog2_price.quotes_data['regularMarketPrice']
print("Price of dog2 is", dog2price, "\n")

#dog3 price
dog3 = dogs_of_dow[2]
print("dog3 is",dog3)
dog3_price = Pinance(dog3)
dog3_price.get_quotes()
dog3price = dog3_price.quotes_data['regularMarketPrice']
print("Price of dog3 is", dog3price ,"\n")

#dog4 price
dog4 = dogs_of_dow[3]
print("dog4 is",dog4)
dog4_price = Pinance(dog4)
dog4_price.get_quotes()
dog4price = dog4_price.quotes_data['regularMarketPrice']
print("Price of dog4 is", dog4price ,"\n")

#dog5 price
dog5 = dogs_of_dow[4]
print("dog5 is",dog5)
dog5_price = Pinance(dog5)
dog5_price.get_quotes()
dog5price = dog5_price.quotes_data['regularMarketPrice']
print("Price of dog5 is", dog5price,"\n")

#dog6 price
dog6 = dogs_of_dow[5]
print("dog6 is",dog6)
dog6_price = Pinance(dog6)
dog6_price.get_quotes()
dog6price = dog6_price.quotes_data['regularMarketPrice']
print("Price of dog6 is", dog6price,"\n")

#dog7 price
dog7 = dogs_of_dow[6]
print("dog7 is",dog7)
dog7_price = Pinance(dog7)
dog7_price.get_quotes()
dog7price = dog7_price.quotes_data['regularMarketPrice']
print("Price of dog7 is", dog7price,"\n")

#dog8 price
dog8 = dogs_of_dow[7]
print("dog8 is",dog8)
dog8_price = Pinance(dog8)
dog8_price.get_quotes()
dog8price = dog8_price.quotes_data['regularMarketPrice']
print("Price of dog8 is", dog8price,"\n")

#dog9 price
dog9 = dogs_of_dow[8]
print("dog9 is",dog9)
dog9_price = Pinance(dog9)
dog9_price.get_quotes()
dog9price = dog9_price.quotes_data['regularMarketPrice']
print("Price of dog9 is", dog9price,"\n")

#dog10 price
dog10 = dogs_of_dow[9]
print("dog10 is",dog10)
dog10_price = Pinance(dog10)
dog10_price.get_quotes()
dog10price = dog10_price.quotes_data['regularMarketPrice']
print("Price of dog10 is", dog10price,"\n")



dog1shares_tobuy = stock_allocation//dog1price
dog2shares_tobuy = stock_allocation//dog2price
dog3shares_tobuy = stock_allocation//dog3price
dog4shares_tobuy = stock_allocation//dog4price
dog5shares_tobuy = stock_allocation//dog5price
dog6shares_tobuy = stock_allocation//dog6price
dog7shares_tobuy = stock_allocation//dog7price
dog8shares_tobuy = stock_allocation//dog8price
dog9shares_tobuy = stock_allocation//dog9price
dog10shares_tobuy = stock_allocation//dog10price


# Create a stock class.
class Stock(): 
	def __init__(self, symbol):
			self.symbol = symbol
			self.position = 0
		
# Function to buy and add shares to stock.	
	def buy_stock(self, shares_bought):
		self.position += shares_bought
		AshishM_TradingAccount.balance -= stock_allocation

# Function to sell and subtract shares from stock.
	def sell_stock(self, shares_sold):
		self.position -= shares_sold


# The default URL ends in / ("my-website.com/").
@app.route('/')

def run():
    dogs_of_dow = ["VZ", "IBM", "XOM", "GE", "CVX", "KO", "PG", "PFE", "MRK", "CSCO"]
    stockList = {}
    for symbol in dogs_of_dow:
        newStock = Stock(symbol)
        stockList.update({
			symbol: newStock
		})
    return stockList

def buyStocks(stockLibrary, amount):
	for stock in stockLibrary.keys():
		stockLibrary[stock].buy_stock(amount)

stockLibrary = run()



stockLibrary[dogs_of_dow[0]].buy_stock(dog1shares_tobuy)
stockLibrary[dogs_of_dow[1]].buy_stock(dog2shares_tobuy)
stockLibrary[dogs_of_dow[2]].buy_stock(dog3shares_tobuy)
stockLibrary[dogs_of_dow[3]].buy_stock(dog4shares_tobuy)
stockLibrary[dogs_of_dow[4]].buy_stock(dog5shares_tobuy)
stockLibrary[dogs_of_dow[5]].buy_stock(dog6shares_tobuy)
stockLibrary[dogs_of_dow[6]].buy_stock(dog7shares_tobuy)
stockLibrary[dogs_of_dow[7]].buy_stock(dog8shares_tobuy)
stockLibrary[dogs_of_dow[8]].buy_stock(dog9shares_tobuy)
stockLibrary[dogs_of_dow[9]].buy_stock(dog10shares_tobuy)



print("Buy", stockLibrary[dogs_of_dow[0]].position, "shares of", dog1)
print("Buy", stockLibrary[dogs_of_dow[1]].position, "shares of", dog2)
print("Buy", stockLibrary[dogs_of_dow[2]].position, "shares of", dog3)
print("Buy", stockLibrary[dogs_of_dow[3]].position, "shares of", dog4)
print("Buy", stockLibrary[dogs_of_dow[4]].position, "shares of", dog5)
print("Buy", stockLibrary[dogs_of_dow[5]].position, "shares of", dog6)
print("Buy", stockLibrary[dogs_of_dow[6]].position, "shares of", dog7)
print("Buy", stockLibrary[dogs_of_dow[7]].position, "shares of", dog8)
print("Buy", stockLibrary[dogs_of_dow[8]].position, "shares of", dog9)
print("Buy", stockLibrary[dogs_of_dow[9]].position, "shares of", dog10)

print("ashish")


if __name__ == '__main__':
    app.run(debug=True)
################################################################################### Need to convert each 	
#dogs_of_dow = ["VZ", "IBM", "XOM", "GE", "CVX", "KO", "PG", "PFE", "MRK", "CSCO"]# stock in this list
################################################################################### to Stock objects.



''' Three end points:
1. Postions Report
	- Shows positions that the fund holds and how many shares for each position.
	- Can show position by each stock adding the symbol into the URL. 

2. Stock information:
	- Shows basic stock details for all of the stocks in the list. 
	- Can show details for each stock by inputting the symbol. 

3. Adding money:
	- Adds money into the bank accounts. 
	- Subracts money from the bank accounts.'''


