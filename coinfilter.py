import collections
import config
from decimal import *
from utils import numfun

reduced_arbi_dict = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict))

def get_interesting_coins(arbi_dict):
	"""
	This method gets a list of potential coins you might wanna trade -THIS IS THE MAIN FUNCTION HERE
	"""
	reduced_arbi_dict = remove_lonely_coins(arbi_dict)
	best_buys = get_best_buys(reduced_arbi_dict)
	return best_buys


def remove_lonely_coins(arbi_dict):
	"""
	This function removes coins that are present only in one exchange and returns a reduced dictionary
	"""
	for coin, exchange in arbi_dict.items():
		if len(exchange) > 1:
			reduced_arbi_dict[coin] = exchange
	return reduced_arbi_dict 


def get_best_buys(reduced_arbi_dict):
	"""
	Return a new dict with best coins to buy containing which exchange to buy in and where to sell at, and the prices 
	"""	
	best_buy = {}
	for coin, exchange in reduced_arbi_dict.items():
		ask_low = get_lowest_ask(exchange)
		high_bid = get_highest_bid(exchange)
		per_diff = numfun.get_percent_difference(Decimal(high_bid[0]), Decimal(ask_low[0]))
		if per_diff >= config.MIN_PERCENT_DIFFERENCE and per_diff <= config.MAX_PERCENT_DIFFERENCE:
			best_buy_dict = {}
			best_buy_dict[config.PRICE_TYPE_ASK] = '{:.9f}'.format(ask_low[0])
			best_buy_dict['BUY_EXCHANGE'] = ask_low[1]
			best_buy_dict[config.PRICE_TYPE_BID] = '{:.9f}'.format(high_bid[0])
			best_buy_dict['SELL_EXCHANGE'] = high_bid[1]
			best_buy_dict['PERCENT_DIFFERENCE'] = str(per_diff)
			best_buy[coin] = best_buy_dict
	return best_buy


def get_lowest_ask(exchanges_dict_list):
	"""
	This is where you buy your coin. 

	Returns a tuple containing the price and the exchange (Exchange, Price)
	"""
	lowest_ask_price = 0
	lowest_ask_exchange = ''
	for exchange_name, exchange in exchanges_dict_list.items():
		if exchange[config.PRICE_TYPE_ASK] is not None:
			if lowest_ask_price == 0 or Decimal(exchange[config.PRICE_TYPE_ASK]) < lowest_ask_price:
				lowest_ask_price = Decimal(exchange[config.PRICE_TYPE_ASK])
				lowest_ask_exchange = exchange_name

	return (lowest_ask_price, lowest_ask_exchange)


def get_highest_bid(exchanges_dict_list):
	"""
	This is where you sell your coin

	Returns a tuple containing the price and the exchange (Exchange, Price)
	"""
	highest_bid_price = 0
	highest_bid_exchange = ''
	for exchange_name, exchange in exchanges_dict_list.items():
		if exchange[config.PRICE_TYPE_BID] is not None:
			if highest_bid_price == 0 or Decimal(exchange[config.PRICE_TYPE_BID]) > highest_bid_price:
				highest_bid_price = Decimal(exchange[config.PRICE_TYPE_BID])
				highest_bid_exchange = exchange_name
	return (highest_bid_price, highest_bid_exchange)
