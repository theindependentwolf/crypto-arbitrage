from crypto.cryptopia import Cryptopia
from crypto.bittrex import Bittrex
from crypto.hitbtc import Hitbtc
from crypto.binance import Binance
from crypto.kucoin import Kucoin
import collections
from decimal import *
from utils import numfun
import json
import config


arbi_dict = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict))

def get_all_coin_info():
	"""
	Get the prices of coins from different exchanges and store it in the arbi_dict dictionary
	"""
	get_cryptopia_info()
	get_bittrex_info()
	get_hitbtc_info()
	get_binance_info()
	get_kucoin_info()
	return arbi_dict



def get_binance_info():
	"""
	Get Binance Info and store it in the combined dictionary
	"""
	binance = Binance()
	#Get binance prices and other info from the Binance API
	binance_info_list = binance.get_markets()
	#Check if response is not null and get all binance info of coin
	if type(binance_info_list) is list and len(binance_info_list) > 0:
		#Dictionary to store binance info about a certain coin		
		for coin_info_dict in binance_info_list:
			if coin_info_dict['symbol'][-3:] == 'BTC':
				binance_dict = {}
				binance_dict[config.PRICE_TYPE_ASK] = coin_info_dict[binance.binance_vars[config.PRICE_TYPE_ASK]]
				binance_dict[config.PRICE_TYPE_LAST] = coin_info_dict[binance.binance_vars[config.PRICE_TYPE_LAST]]
				binance_dict[config.PRICE_TYPE_BID] = coin_info_dict[binance.binance_vars[config.PRICE_TYPE_BID]]
				arbi_dict[coin_info_dict['symbol'][:-3]]['binance'] = binance_dict


def get_cryptopia_info():
	"""
	Get the prices in Cryptopia
	"""
	cryptopia = Cryptopia()
	cryptopia_prices = cryptopia.get_markets('BTC', None)
	if cryptopia_prices and cryptopia_prices['Success'] == True:		
		price_dict_list = cryptopia_prices['Data']
		for price_dict in price_dict_list:
			cryptopia_dict = {}
			cryptopia_dict[config.PRICE_TYPE_ASK] = '{:.9f}'.format(price_dict[cryptopia.cryptopia_vars[config.PRICE_TYPE_ASK]])
			cryptopia_dict[config.PRICE_TYPE_BID] = '{:.9f}'.format(price_dict[cryptopia.cryptopia_vars[config.PRICE_TYPE_BID]])
			cryptopia_dict[config.PRICE_TYPE_LAST] = '{:.9f}'.format(price_dict[cryptopia.cryptopia_vars[config.PRICE_TYPE_LAST]])
			arbi_dict[price_dict['Label'].split('/')[0]]['cryptopia'] = cryptopia_dict
	else:
		print("An Error has occurred while retrieving prices from Cryptopia")


def get_hitbtc_info():
	"""
	Get HitBTC prices
	"""
	hitbtc = Hitbtc()
	hitbtc_prices = hitbtc.get_markets()

	if type(hitbtc_prices) is list and len(hitbtc_prices) > 0:		
		for price_dict in hitbtc_prices:			
			if price_dict['symbol'][-3:] == 'BTC':
				hitbtc_dict = {}
				hitbtc_dict[config.PRICE_TYPE_ASK] =  price_dict[hitbtc.hitbtc_vars[config.PRICE_TYPE_ASK]]
				hitbtc_dict[config.PRICE_TYPE_BID] =  price_dict[hitbtc.hitbtc_vars[config.PRICE_TYPE_BID]]
				hitbtc_dict[config.PRICE_TYPE_LAST] =  price_dict[hitbtc.hitbtc_vars[config.PRICE_TYPE_LAST]]
				arbi_dict[price_dict['symbol'][:-3]]['hitbtc'] = hitbtc_dict


def get_bittrex_info():
	"""
	Get the prices in bittrex
	"""
	bittrex = Bittrex()
	bittrex_prices = bittrex.get_markets()
	if bittrex_prices and bittrex_prices['success'] == True:
		price_dict_list = bittrex_prices['result']		
		for price_dict in price_dict_list:
			if price_dict['MarketName'].split('-')[0] == 'BTC':
				bittrex_dict = {}
				bittrex_dict[config.PRICE_TYPE_ASK] = '{:.9f}'.format(price_dict[bittrex.bittrex_vars[config.PRICE_TYPE_ASK]])
				bittrex_dict[config.PRICE_TYPE_BID] = '{:.9f}'.format(price_dict[bittrex.bittrex_vars[config.PRICE_TYPE_BID]])
				bittrex_dict[config.PRICE_TYPE_LAST] = '{:.9f}'.format(price_dict[bittrex.bittrex_vars[config.PRICE_TYPE_LAST]])
				arbi_dict[price_dict['MarketName'].split('-')[1]]['bittrex'] = bittrex_dict


def get_kucoin_info():
	"""
	Get the prices in Kucoin
	"""
	kucoin = Kucoin()
	kucoin_prices = kucoin.get_markets()
	if kucoin_prices and kucoin_prices['success'] == True:		
		price_dict_list = kucoin_prices['data']
		for price_dict in price_dict_list:
			if price_dict['coinTypePair'] == 'BTC':
				kucoin_dict = {}
				kucoin_dict[config.PRICE_TYPE_ASK] = '{:.9f}'.format(price_dict[kucoin.kucoin_vars[config.PRICE_TYPE_ASK]])
				kucoin_dict[config.PRICE_TYPE_BID] = '{:.9f}'.format(price_dict[kucoin.kucoin_vars[config.PRICE_TYPE_BID]])
				kucoin_dict[config.PRICE_TYPE_LAST] = '{:.9f}'.format(price_dict[kucoin.kucoin_vars[config.PRICE_TYPE_LAST]])
				arbi_dict[price_dict['coinType']]['kucoin'] = kucoin_dict
	else:
		print("An Error has occurred while retrieving prices from kucoin")


