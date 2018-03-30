import urllib.request
import requests
import json
import sys


hitbtc_url = {
	"markets":"https://api.hitbtc.com/api/2/public/ticker",
    "address":"https://api.hitbtc.com/api/2/account/crypto/address/"
}



class Hitbtc:
	"""
	Contains the different Cryptopia methods
	"""

	hitbtc_vars = {
		"ASK":"ask",
		"BID":"bid",
		"LAST":"last"
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


	def get_json_private_get(self, url):
		"""
		Get JSON data for requests that need keys
		"""
		response = requests.get(url, auth=self.auth)
		return response.json()


	def get_markets(self):
		"""
		Get the market values 
		"""
		url = hitbtc_url['markets']
		json_data = self.get_json(url)
		return json_data


	def get_address(self, currency):
		"""
		Get deposit address of a currency
		"""
		url = hitbtc_url['address'] + currency
		json_data = self.get_json_private_get(url)
		return json_data



