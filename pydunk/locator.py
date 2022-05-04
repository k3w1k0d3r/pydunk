from geopy.geocoders import Nominatim
from .api import API
from .store import Store
class Location():
	def __init__(self, address=None, lat_long=None, user_agent="pyDunk"):
		self.geolocator = Nominatim(user_agent=user_agent)
		self.location = None
		if(address is not None):
			self.location = self.geolocator.geocode(address)
		if(lat_long is not None):
			self.location = self.geolocator.reverse("%s, %s"%lat_long)
	def update(self, address=None, lat_long=None):
		self.location = None
		if(address is not None):
			self.location = self.geolocator.geocode(address)
		if(lat_long is not None):
			self.location = self.geolocator.reverse("%s, %s"%lat_long)
class Locator():
	def __init__(self, location: Location=None, api: API=None):
		self.location = location
		self.api = api
		if(self.api is None):
			self.api = API()
	def update(self, location: Location):
		self.location = location
	def get_stores(self, radius=25, max_matches=30):
		data = {"service": "DSL", "origin": "%s,%s"%(self.location.location.raw["lat"], self.location.location.raw["lon"]), "radius": str(radius), "maxMatches": str(max_matches), "pageSize": "1", "units": "m", "ambiguities": "ignore"}
		res = self.api.post("/bin/servlet/dsl", data)
		stores = []
		for i in res["data"]["storeAttributes"]:
			stores.append(Store())
		return stores
