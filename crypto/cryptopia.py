import urllib.request
import json


cryptopia_url = {
	"currency":"https://www.cryptopia.co.nz/api/GetCurrencies",
	"pair":"https://www.cryptopia.co.nz/api/GetTradePairs",
	"markets":"https://www.cryptopia.co.nz/api/GetMarkets",
	"history":"https://www.cryptopia.co.nz/api/GetMarketHistory/100",
	"market":"https://www.cryptopia.co.nz/api/GetMarket",
}

class Cryptopia:
	"""
	Contains the different Cryptopia methods
	"""

	cryptopia_vars = {
		"ASK":"AskPrice",
		"BID":"BidPrice",
		"LAST":"LastPrice"
	}

	def get_json(self, url):
		"""
		Get the json data for the given URL in dictionary format
		"""
		html = urllib.request.urlopen(url)
		encoding = html.info().get_content_charset('utf8')
		json_string = html.read().decode(encoding)
		json_dict = json.loads(json_string) 
		return json_dict


	def get_markets(self, currency, time):
		"""
		Get the market values of specified currency
		"""
		url = cryptopia_url['markets']
		if currency:
			url += str('/') + str(currency)
		if time:
			url += str('/') + str(time)
		json_data = self.get_json(url)
		return json_data


