import urllib.request
import json


bittrex_url = {
	"markets":"https://bittrex.com/api/v1.1/public/getmarketsummaries"
}

class Bittrex:
	"""
	Contains the different Cryptopia methods
	"""

	bittrex_vars = {
		"ASK":"Ask",
		"BID":"Bid",
		"LAST":"Last"
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
		url = bittrex_url['markets']
		json_data = self.get_json(url)
		return json_data


