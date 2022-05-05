class Item():
	def __init__(self, name, url):
		self.url = url
		self.name = name
class Menu():
	def __init__(self, language="en", url="https://www.dunkindonuts.com"):
		self.language = language
		self.url = url
		self.items = self.scrape()
	def scrape(self): #the FUCKING assholes at dd decided to just send over static html for the menu page instead of using an API, so now I need to fucking scrape html god fucking damnit
		return []
