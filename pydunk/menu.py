import re
import requests
class Item():
	def __init__(self, url):
		self.url = url
class Menu():
	def __init__(self, language="en", url="https://www.dunkindonuts.com"):
		self.language = language
		self.url = url
		self.items = self.scrape()
	def scrape(self): #the FUCKING assholes at dd decided to just send over static html for the menu page instead of using an API, so now I need to fucking scrape html god fucking damnit
		out = []
		res = requests.get(self.url+"/"+self.language+"/menu").text
		urls = [i[3:-1] for i in re.findall("f=\"\\/%s\\/menu\\/(?!nutrition).*?\""%self.language, res)]
		for i in urls:
			res = requests.get(self.url+i).text
			items = [Item(i[3:-1]) for i in re.findall("f=\"\\/%s\\/menu\\/.*\\/product.*?\""%self.language, res)]
			out+=items
		return out
