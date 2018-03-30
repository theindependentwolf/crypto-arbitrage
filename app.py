# from crypto.cryptopia import Cryptopia
# from crypto.bittrex import Bittrex
# from crypto.hitbtc import Hitbtc
# from crypto.binance import Binance
# import collections
# from decimal import *
# from utils import numfun
import json
import config
import coininfo
import coinfilter


def pretty_print(arbi_dict):
	"""
	pretty print the arbi dict dictionary
	"""
	print(json.dumps(arbi_dict,indent=4))


def arbitrage():
	"""
	List of potential arbitrage
	"""
	arbi_dict = coininfo.get_all_coin_info()
	interesting = coinfilter.get_interesting_coins(arbi_dict)
	pretty_print(interesting)
	# pretty_print(arbi_dict)


if __name__ == '__main__':
	arbitrage()
