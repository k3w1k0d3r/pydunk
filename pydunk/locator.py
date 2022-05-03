from geopy.geocoders import Nominatim
class Location():
	def __init__(self, address=None, lat_long=None, user_agent="pyDunk"):
		self.eolocator = Nominatim(user_agent=user_agent)
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
	def __init__(self, location: Location=None):
		pass
