import urllib.request
import json


binance_url = {
	"markets":"https://api.binance.com/api/v1/ticker/24hr"
}

class Binance:
	"""
	Contains the different Binance functions
	"""

	binance_vars = {
		"ASK":"askPrice",
		"BID":"bidPrice",
		"LAST":"lastPrice"
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


	def get_markets(self):
		"""
		Get the market values of specified currency (BTC, LTC, USDT)
		"""
		url = binance_url['markets']
		json_data = self.get_json(url)
		return json_data

	