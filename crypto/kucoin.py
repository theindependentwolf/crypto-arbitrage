import urllib.request
import json


kucoin_url = {
	"markets":"https://api.kucoin.com/v1/open/tick"
}

class Kucoin:
	"""
	Contains the different Cryptopia methods
	"""

	kucoin_vars = {
		"ASK":"sell",
		"BID":"buy",
		"LAST":"lastDealPrice"
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
		Get the market values of specified currency
		"""
		url = kucoin_url['markets']
		json_data = self.get_json(url)
		return json_data

