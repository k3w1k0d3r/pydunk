import requests
class API():
	def __init__(self, url="https://www.dunkindonuts.com"):
		self.url = url
	def post(self, path, data):
		s = requests.post(self.url+path, data=data)
		return s.json()
